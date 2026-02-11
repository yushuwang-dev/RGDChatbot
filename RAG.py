"""
RAG (Retrieval-Augmented Generation) System using Ollama
Supports document loading, chunking, embedding, and retrieval-augmented generation
"""

import ollama
import chromadb
from chromadb.config import Settings
from typing import List, Dict, Optional
import os
from pathlib import Path
import pdfplumber
import PyPDF2
import re
import json


class RAGSystem:
    """
    A RAG system that uses Ollama for embeddings and LLM generation,
    and ChromaDB for vector storage and retrieval.
    """
    
    def __init__(
        self,
        collection_name: str = "rag_documents",
        embedding_model: str = "mxbai-embed-large:latest", 
        llm_model: str = "llama3.2",
        persist_directory: str = "./chroma_db",
        embedding_host: str = "http://grudge.rgd.mcw.edu:11434",
        llm_host: str = "http://grudge.rgd.mcw.edu:11434"
    ):
        """
        Initialize the RAG system.
        
        Args:
            collection_name: Name of the ChromaDB collection
            embedding_model: Ollama model for embeddings
            llm_model: Ollama model for text generation
            persist_directory: Directory to persist ChromaDB data
            embedding_host: Ollama server URL for embeddings
            llm_host: Ollama server URL for chat/generation
        """
        self.embedding_model = embedding_model
        self.llm_model = llm_model
        self.persist_directory = persist_directory
        self.embedding_host = embedding_host
        self.llm_host = llm_host
        self.embedding_client = ollama.Client(host=embedding_host)
        self.llm_client = ollama.Client(host=llm_host)
        
        # Initialize ChromaDB client
        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=Settings(anonymized_telemetry=False)
        )
        
        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )
        
        # Dictionary to store links with annotations
        self.links_dict: Dict[str, Dict] = {}
        self.links_file = os.path.join(persist_directory, "links_dict.json")
        self._load_links()
        
        print(f"✓ RAG System initialized")
        print(f"  - Embedding model: {embedding_model}")
        print(f"  - LLM model: {llm_model}")
        print(f"  - Embedding host: {embedding_host}")
        print(f"  - LLM host: {llm_host}")
        print(f"  - Collection: {collection_name}")
        print(f"  - Links dictionary: {len(self.links_dict)} links loaded")
    
    def _chunk_text(self, text: str, chunk_size: int = 1500, chunk_overlap: int = 300) -> List[str]:
        """
        Split text into overlapping chunks.
        
        Args:
            text: Text to chunk
            chunk_size: Size of each chunk in characters
            chunk_overlap: Overlap between chunks in characters
            
        Returns:
            List of text chunks
        """
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            
            if end >= len(text):
                break
                
            start = end - chunk_overlap
        
        return chunks
    
    def _get_embedding(self, text: str) -> List[float]:
        """
        Get embedding for a text using Ollama.
        
        Args:
            text: Text to embed
            
        Returns:
            Embedding vector
        """
        try:
            response = self.embedding_client.embeddings(model=self.embedding_model, prompt=text)
            return response['embedding']
        except Exception as e:
            print(f"Error getting embedding: {e}")
            raise
    
    def add_documents(self, documents: List[str], metadatas: Optional[List[Dict]] = None):
        """
        Add documents to the vector store.
        
        Args:
            documents: List of document texts
            metadatas: Optional list of metadata dictionaries for each document
        """
        if metadatas is None:
            metadatas = [{}] * len(documents)
        
        all_chunks = []
        all_metadatas = []
        chunk_ids = []
        
        chunk_idx = 0
        for doc_idx, doc in enumerate(documents):
            chunks = self._chunk_text(doc)
            
            for chunk in chunks:
                all_chunks.append(chunk)
                metadata = metadatas[doc_idx].copy()
                metadata['chunk_index'] = chunk_idx
                metadata['doc_index'] = doc_idx
                all_metadatas.append(metadata)
                chunk_ids.append(f"chunk_{chunk_idx}")
                chunk_idx += 1
        
        print(f"Processing {len(all_chunks)} chunks...")
        
        # Get embeddings for all chunks
        embeddings = []
        for i, chunk in enumerate(all_chunks):
            if (i + 1) % 10 == 0:
                print(f"  Embedded {i + 1}/{len(all_chunks)} chunks...")
            embedding = self._get_embedding(chunk)
            embeddings.append(embedding)
        
        # Add to ChromaDB
        self.collection.add(
            ids=chunk_ids,
            embeddings=embeddings,
            documents=all_chunks,
            metadatas=all_metadatas
        )
        
        print(f"✓ Added {len(all_chunks)} chunks to vector store")
    
    def _extract_urls_from_text(self, text: str, context_window: int = 200) -> List[Dict]:
        """
        Extract URLs from text with surrounding context for annotation.
        
        Args:
            text: Text to extract URLs from
            context_window: Number of characters before/after URL to capture as context
            
        Returns:
            List of dictionaries with URL, context, and annotation
        """
        urls = []
        
        # URL pattern - matches http, https, www, and common domains
        url_pattern = r'(https?://[^\s<>"{}|\\^`\[\]]+|www\.[^\s<>"{}|\\^`\[\]]+|rgd\.mcw\.edu[^\s<>"{}|\\^`\[\]]*|doi\.org/[^\s<>"{}|\\^`\[\]]+)'
        
        for match in re.finditer(url_pattern, text, re.IGNORECASE):
            url = match.group(0)
            start_pos = match.start()
            end_pos = match.end()
            
            # Get context around the URL
            context_start = max(0, start_pos - context_window)
            context_end = min(len(text), end_pos + context_window)
            context = text[context_start:context_end].strip()
            
            # Try to extract a description/annotation from context
            # Look for patterns like "available at", "see", "visit", etc.
            annotation = ""
            context_lower = context.lower()
            if any(phrase in context_lower for phrase in ['available at', 'visit', 'access', 'see', 'download', 'find']):
                # Extract sentence or phrase containing the URL
                sentences = re.split(r'[.!?]\s+', context)
                for sentence in sentences:
                    if url.lower() in sentence.lower():
                        annotation = sentence.strip()
                        break
            
            # If no annotation found, use a snippet of context
            if not annotation:
                annotation = context[:150] + "..." if len(context) > 150 else context
            
            urls.append({
                'url': url,
                'context': context,
                'annotation': annotation,
                'position': start_pos
            })
        
        return urls
    
    def _load_links(self):
        """Load links dictionary from file if it exists."""
        if os.path.exists(self.links_file):
            try:
                with open(self.links_file, 'r', encoding='utf-8') as f:
                    self.links_dict = json.load(f)
            except Exception as e:
                print(f"Warning: Could not load links dictionary: {e}")
                self.links_dict = {}
        else:
            self.links_dict = {}
    
    def _save_links(self):
        """Save links dictionary to file."""
        try:
            os.makedirs(os.path.dirname(self.links_file), exist_ok=True)
            with open(self.links_file, 'w', encoding='utf-8') as f:
                json.dump(self.links_dict, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Could not save links dictionary: {e}")
    
    def _find_relevant_links(self, query: str, max_links: int = 3) -> List[Dict]:
        """
        Find relevant links for a query by matching against link annotations.
        
        Args:
            query: User query
            max_links: Maximum number of links to return
            
        Returns:
            List of relevant link dictionaries
        """
        query_lower = query.lower()
        relevant_links = []
        
        # Score links based on keyword matching
        for url, link_info in self.links_dict.items():
            score = 0
            annotation = link_info.get('annotation', '').lower()
            context = link_info.get('context', '').lower()
            
            # Check if query keywords appear in annotation or context
            query_words = set(query_lower.split())
            annotation_words = set(annotation.split())
            context_words = set(context.split())
            
            # Score based on word overlap
            score += len(query_words & annotation_words) * 2
            score += len(query_words & context_words)
            
            # Boost score for specific keywords
            if any(word in annotation or word in context for word in ['download', 'access', 'tool', 'database', 'portal']):
                if any(word in query_lower for word in ['download', 'access', 'tool', 'database', 'portal', 'link', 'url']):
                    score += 3
            
            if score > 0:
                relevant_links.append({
                    'url': url,
                    'annotation': link_info.get('annotation', ''),
                    'score': score
                })
        
        # Sort by score and return top links
        relevant_links.sort(key=lambda x: x['score'], reverse=True)
        return relevant_links[:max_links]
    
    def _extract_text_from_pdf(self, file_path: str) -> str:
        """
        Extract text from a PDF file using pdfplumber (primary) or PyPDF2 (fallback).
        
        Args:
            file_path: Path to the PDF file
            
        Returns:
            Extracted text from the PDF
        """
        text = ""
        
        # Try pdfplumber first (better text extraction)
        try:
            with pdfplumber.open(file_path) as pdf:
                pages_text = []
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        pages_text.append(page_text)
                text = "\n\n".join(pages_text)
                if text:
                    return text
        except Exception as e:
            print(f"Warning: pdfplumber failed for {file_path}: {e}, trying PyPDF2...")
        
        # Fallback to PyPDF2
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                pages_text = []
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        pages_text.append(page_text)
                text = "\n\n".join(pages_text)
        except Exception as e:
            print(f"Error extracting text from PDF {file_path}: {e}")
            raise
        
        return text
    
    def add_documents_from_files(self, file_paths: List[str]):
        """
        Load documents from files (text files or PDFs) and add to vector store.
        
        Args:
            file_paths: List of file paths to load (supports .txt, .pdf, and other text files)
        """
        documents = []
        metadatas = []
        
        for file_path in file_paths:
            path = Path(file_path)
            if not path.exists():
                print(f"Warning: File not found: {file_path}")
                continue
            
            try:
                # Check if it's a PDF file
                if path.suffix.lower() == '.pdf':
                    print(f"Extracting text from PDF: {path.name}...")
                    content = self._extract_text_from_pdf(str(path))
                    if not content.strip():
                        print(f"Warning: No text extracted from {file_path}")
                        continue
                    
                    # Extract URLs from the content
                    urls = self._extract_urls_from_text(content)
                    if urls:
                        print(f"    Found {len(urls)} link(s)")
                        for url_info in urls:
                            url = url_info['url']
                            if url not in self.links_dict:
                                self.links_dict[url] = {
                                    'annotation': url_info['annotation'],
                                    'context': url_info['context'],
                                    'source_file': path.name
                                }
                    
                    documents.append(content)
                    metadatas.append({
                        'source': str(path),
                        'filename': path.name,
                        'file_type': 'pdf',
                        'pages': len(content.split('\n\n'))  # Approximate page count
                    })
                    print(f"  ✓ Extracted {len(content)} characters from {path.name}")
                else:
                    # Handle text files
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # Extract URLs from text files too
                        urls = self._extract_urls_from_text(content)
                        if urls:
                            for url_info in urls:
                                url = url_info['url']
                                if url not in self.links_dict:
                                    self.links_dict[url] = {
                                        'annotation': url_info['annotation'],
                                        'context': url_info['context'],
                                        'source_file': path.name
                                    }
                        
                        documents.append(content)
                        metadatas.append({
                            'source': str(path),
                            'filename': path.name,
                            'file_type': 'text'
                        })
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
        
        if documents:
            print(f"\nProcessing {len(documents)} document(s)...")
            self.add_documents(documents, metadatas)
            
            # Save links dictionary after processing
            if self.links_dict:
                self._save_links()
                print(f"  ✓ Saved {len(self.links_dict)} links to dictionary")
    
    def retrieve(self, query: str, n_results: int = 5, min_similarity: float = 0.0) -> List[Dict]:
        """
        Retrieve relevant documents for a query.
        
        Args:
            query: Query text
            n_results: Number of results to retrieve
            min_similarity: Minimum similarity threshold (0.0 to 1.0, higher = more strict)
            
        Returns:
            List of retrieved documents with metadata
        """
        # Get query embedding
        query_embedding = self._get_embedding(query)
        
        # Query ChromaDB - retrieve more than needed to filter by similarity
        query_n = max(n_results * 2, 10)  # Retrieve more for filtering
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=query_n
        )
        
        retrieved_docs = []
        if results['documents'] and len(results['documents'][0]) > 0:
            for i, doc in enumerate(results['documents'][0]):
                distance = results['distances'][0][i] if results['distances'] else 1.0
                # Convert distance to similarity (cosine distance -> similarity)
                similarity = 1.0 - distance
                
                # Filter by minimum similarity
                if similarity >= min_similarity:
                    retrieved_docs.append({
                        'document': doc,
                        'metadata': results['metadatas'][0][i] if results['metadatas'] else {},
                        'distance': distance,
                        'similarity': similarity
                    })
        
        # Sort by similarity (highest first) and return top n_results
        retrieved_docs.sort(key=lambda x: x.get('similarity', 0), reverse=True)
        return retrieved_docs[:n_results]
    
    def generate(self, query: str, n_results: int = 5, system_prompt: Optional[str] = None, 
                 min_similarity: float = 0.3, include_sources: bool = False,
                 temperature: float = 0.0, seed: Optional[int] = None) -> str:
        """
        Generate a response using RAG (retrieve relevant context, then generate).
        
        Args:
            query: User query
            n_results: Number of relevant chunks to retrieve (default: 5, increased for better accuracy)
            system_prompt: Optional custom system prompt
            min_similarity: Minimum similarity threshold for retrieved chunks (0.0-1.0)
            include_sources: Whether to include source information in the response
            
        Returns:
            Generated response
        """
        # Retrieve relevant documents with similarity filtering
        retrieved_docs = self.retrieve(query, n_results=n_results, min_similarity=min_similarity)
        
        if not retrieved_docs:
            return "I cannot find information about this in the available documents."
        
        # Build context from retrieved documents with source attribution
        context_parts = []
        sources = []
        for i, doc in enumerate(retrieved_docs, 1):
            doc_text = doc['document']
            filename = doc['metadata'].get('filename', 'Unknown')
            similarity = doc.get('similarity', 0)
            
            # Format context with source info
            context_parts.append(f"[Source {i}: {filename}]\n{doc_text}")
            sources.append({
                'filename': filename,
                'similarity': similarity,
                'preview': doc_text[:100] + '...' if len(doc_text) > 100 else doc_text
            })
        
        context = "\n\n---\n\n".join(context_parts)
        
        # Improved system prompt - focused on short, clear answers
        if system_prompt is None:
            system_prompt = """You are a helpful assistant that provides short, clear answers based ONLY on the provided context.

IMPORTANT INSTRUCTIONS:
1. Answer the question using ONLY the information in the provided context
2. Keep your answer SHORT and CLEAR - be concise and direct
3. If the context doesn't contain enough information to answer the question, simply say "I cannot find information about this in the available documents" or similar
4. Do not make up information or use knowledge outside the provided context
5. Do not provide long explanations or disclaimers - just answer directly"""
        
        # Build the prompt with better formatting
        prompt = f"""Based on the following context, provide a SHORT and CLEAR answer to the question.

CONTEXT:
{context}

QUESTION: {query}

Answer (be brief and direct):"""
        
        # Generate response using Ollama
        try:
            options: Dict[str, object] = {"temperature": temperature}
            if seed is not None:
                options["seed"] = seed

            response = self.llm_client.chat(
                model=self.llm_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                options=options
            )
            answer = response['message']['content'].strip()
            
            # Check if the answer indicates no information found
            no_info_phrases = [
                "cannot find",
                "don't have",
                "not available",
                "not found",
                "no information",
                "doesn't contain"
            ]
            
            # If answer suggests no info and similarity is low, return simple message
            if any(phrase in answer.lower() for phrase in no_info_phrases):
                if sources and sources[0].get('similarity', 0) < 0.4:
                    return "I cannot find information about this in the available documents."
            
            return answer
        except Exception as e:
            return f"Error generating response: {e}"
    
    def get_links_dict(self) -> Dict[str, Dict]:
        """
        Get the links dictionary.
        
        Returns:
            Dictionary of URLs with their annotations
        """
        return self.links_dict
    
    def print_links(self, limit: Optional[int] = None):
        """
        Print all links in the dictionary.
        
        Args:
            limit: Maximum number of links to print (None for all)
        """
        links_list = list(self.links_dict.items())
        if limit:
            links_list = links_list[:limit]
        
        print(f"\nLinks Dictionary ({len(self.links_dict)} total):")
        print("="*70)
        for i, (url, info) in enumerate(links_list, 1):
            print(f"\n[{i}] {url}")
            print(f"    Annotation: {info.get('annotation', 'N/A')[:100]}...")
            print(f"    Source: {info.get('source_file', 'N/A')}")
    
    def clear_collection(self):
        """Clear all documents from the collection."""
        self.client.delete_collection(self.collection.name)
        self.collection = self.client.get_or_create_collection(
            name=self.collection.name,
            metadata={"hnsw:space": "cosine"}
        )
        print("✓ Collection cleared")


def main():
    """Example usage of the RAG system."""
    # Initialize RAG system
    rag = RAGSystem(
        embedding_model="nomic-embed-text",
        llm_model="llama3.2"
    )
    
    # Example: Add some documents
    documents = [
        "Python is a high-level programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991.",
        "Machine Learning is a subset of artificial intelligence that enables computers to learn from data without being explicitly programmed.",
        "RAG (Retrieval-Augmented Generation) combines information retrieval with language generation to provide more accurate and context-aware responses."
    ]
    
    print("\n" + "="*50)
    print("Adding documents to knowledge base...")
    rag.add_documents(documents)
    
    # Example: Query the system
    print("\n" + "="*50)
    print("Querying the RAG system...")
    query = "What is Python?"
    print(f"Query: {query}\n")
    
    response = rag.generate(query, n_results=2)
    print(f"Response:\n{response}\n")
    
    # Example: Retrieve relevant documents
    print("="*50)
    print("Retrieving relevant documents...")
    retrieved = rag.retrieve("What is machine learning?", n_results=2)
    for i, doc in enumerate(retrieved, 1):
        print(f"\nDocument {i}:")
        print(f"  Content: {doc['document'][:100]}...")
        print(f"  Metadata: {doc['metadata']}")


if __name__ == "__main__":
    main()


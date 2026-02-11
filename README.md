# RAG System with Ollama

A Retrieval-Augmented Generation (RAG) system that uses Ollama for embeddings and LLM generation, with ChromaDB for vector storage.


##  Setup 

1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Remote models:**
   - Uses remote Ollama at `http://grudge.rgd.mcw.edu:11434`

4. **Build the index:**
   ```bash
   python rag_cli.py --build
   ```

5. **Ask questions:**
   ```bash
   python rag_cli.py --question "What is RGD?"
   ```

## Features

- **Document Chunking**: Automatically splits documents into overlapping chunks
- **PDF Support**: Extract text from PDF files automatically
- **Vector Storage**: Uses ChromaDB for efficient similarity search
- **Embeddings**: Uses Ollama embedding models (default: mxbai-embed-large:latest)
- **Generation**: Uses Ollama LLM models for text generation
- **Persistence**: Vector database is persisted to disk

## Configuration

You can customize the RAG system:

```python
rag = RAGSystem(
    collection_name="my_collection",      # ChromaDB collection name
    embedding_model="mxbai-embed-large:latest",   # Ollama embedding model
    llm_model="llama3.2",                 # Ollama LLM model
    persist_directory="./chroma_db"       # Where to store the vector DB
)
```

## Documents Used

You can index any folder. Default is `RGDHelpMarkdown/`.

Examples:
```bash
python rag_cli.py --build --papers-dir RGDHelpMarkdown
python rag_cli.py --build --papers-dir papers
python rag_cli.py --build --papers-dirs RGDHelpMarkdown papers
```

## Embedding Model

Default embedding model is `mxbai-embed-large:latest`.

## CLI Arguments (rag_cli.py)

```bash
--build            Build the index from the documents folder
--papers-dir       Path to documents folder (default: RGDHelpMarkdown)
--collection       ChromaDB collection name (default: rgdhelp_collection)
--embedding-host   Ollama server URL for embeddings (default: http://grudge.rgd.mcw.edu:11434)
--llm-host         Ollama server URL for chat/LLM (default: http://grudge.rgd.mcw.edu:11434)
--llm-model        LLM model name (default: llama3.2)
--question         Ask a single question (string)
--interactive      Start interactive Q&A shell
--n-results        Number of chunks to retrieve (default: 5)
--min-similarity   Minimum similarity threshold (default: 0.3)
--temperature      LLM temperature (default: 0.0)
--seed             LLM seed for deterministic output
--show-context     Print retrieved chunks used for the answer
--papers-dirs      List of document folders to index
```


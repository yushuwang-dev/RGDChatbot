"""
CLI interface for building and querying the RAG system.

Usage examples:
  python rag_cli.py --build
  python rag_cli.py --question "What is RGD?"
  python rag_cli.py --interactive
"""

import argparse
from pathlib import Path
from RAG import RAGSystem


def get_documents_from_folder(folder_path: str):
    """Return all supported documents in a folder."""
    folder = Path(folder_path)
    if not folder.exists():
        return []

    supported_extensions = [".pdf", ".txt", ".md"]
    files = []
    for ext in supported_extensions:
        files.extend(list(folder.glob(f"*{ext}")))

    return sorted([str(f) for f in files])


def build_index(rag: RAGSystem, papers_dir: str):
    """Build the vector index from papers folder."""
    docs = get_documents_from_folder(papers_dir)
    if not docs:
        print(f"No documents found in '{papers_dir}'.")
        return False

    print(f"Found {len(docs)} document(s) in '{papers_dir}'.")
    rag.add_documents_from_files(docs)
    print(f"Index built. Total chunks: {rag.collection.count()}")
    return True


def ask_question(rag: RAGSystem, question: str, n_results: int, min_similarity: float):
    """Ask a single question and print Q/A."""
    answer = rag.generate(
        question,
        n_results=n_results,
        min_similarity=min_similarity,
    )
    print(f"Q: {question}")
    print(f"A: {answer}")


def interactive_shell(rag: RAGSystem, n_results: int, min_similarity: float):
    """Interactive question loop."""
    print("Interactive RAG shell. Type 'exit' to quit.")
    while True:
        try:
            question = input("> ").strip()
        except EOFError:
            print()
            break

        if not question:
            continue

        if question.lower() in {"exit", "quit", "q"}:
            break

        ask_question(rag, question, n_results, min_similarity)
        print()


def main():
    parser = argparse.ArgumentParser(description="RAG CLI")
    parser.add_argument("--build", action="store_true", help="Build index from papers folder")
    parser.add_argument("--papers-dir", default="RGDHelpMarkdown", help="Path to documents folder")
    parser.add_argument("--papers-dirs", nargs="+", help="List of document folders to index")
    parser.add_argument("--collection", default="rgdhelp_collection", help="ChromaDB collection name")
    parser.add_argument("--embedding-host", default="http://grudge.rgd.mcw.edu:11434", help="Ollama server URL for embeddings")
    parser.add_argument("--llm-host", default="http://grudge.rgd.mcw.edu:11434", help="Ollama server URL for chat")
    parser.add_argument("--llm-model", default="llama3.2", help="LLM model name (default: llama3.2)")
    parser.add_argument("--question", help="Ask a single question")
    parser.add_argument("--interactive", action="store_true", help="Run interactive shell")
    parser.add_argument("--n-results", type=int, default=5, help="Number of chunks to retrieve")
    parser.add_argument("--min-similarity", type=float, default=0.3, help="Minimum similarity threshold")
    parser.add_argument("--temperature", type=float, default=0.0, help="LLM temperature (default: 0.0)")
    parser.add_argument("--seed", type=int, default=None, help="LLM seed for deterministic output")
    parser.add_argument("--show-context", action="store_true", help="Show retrieved context chunks")

    args = parser.parse_args()

    rag = RAGSystem(
        collection_name=args.collection,
        embedding_host=args.embedding_host,
        llm_host=args.llm_host,
        llm_model=args.llm_model
    )

    if args.build:
        if args.papers_dirs:
            all_docs = []
            for folder in args.papers_dirs:
                all_docs.extend(get_documents_from_folder(folder))
            if not all_docs:
                print("No documents found in the specified folders.")
                return
            print(f"Found {len(all_docs)} document(s) across {len(args.papers_dirs)} folder(s).")
            rag.add_documents_from_files(sorted(set(all_docs)))
        else:
            build_index(rag, args.papers_dir)

    if args.question:
        if rag.collection.count() == 0:
            print("Collection is empty. Run with --build first.")
            return
        if args.show_context:
            retrieved = rag.retrieve(
                args.question,
                n_results=args.n_results,
                min_similarity=args.min_similarity
            )
            print("Retrieved context:")
            for i, doc in enumerate(retrieved, 1):
                filename = doc.get("metadata", {}).get("filename", "Unknown")
                sim = doc.get("similarity", 0)
                preview = doc.get("document", "")[:200].replace("\n", " ")
                print(f"[{i}] {filename} (sim: {sim:.3f}) {preview}...")
            print()

        answer = rag.generate(
            args.question,
            n_results=args.n_results,
            min_similarity=args.min_similarity,
            temperature=args.temperature,
            seed=args.seed
        )
        print(f"Q: {args.question}")
        print(f"A: {answer}")
        return

    if args.interactive:
        if rag.collection.count() == 0:
            print("Collection is empty. Run with --build first.")
            return
        print("Interactive RAG shell. Type 'exit' to quit.")
        while True:
            try:
                question = input("> ").strip()
            except EOFError:
                print()
                break

            if not question:
                continue

            if question.lower() in {"exit", "quit", "q"}:
                break

            if args.show_context:
                retrieved = rag.retrieve(
                    question,
                    n_results=args.n_results,
                    min_similarity=args.min_similarity
                )
                print("Retrieved context:")
                for i, doc in enumerate(retrieved, 1):
                    filename = doc.get("metadata", {}).get("filename", "Unknown")
                    sim = doc.get("similarity", 0)
                    preview = doc.get("document", "")[:200].replace("\n", " ")
                    print(f"[{i}] {filename} (sim: {sim:.3f}) {preview}...")
                print()

            answer = rag.generate(
                question,
                n_results=args.n_results,
                min_similarity=args.min_similarity,
                temperature=args.temperature,
                seed=args.seed
            )
            print(f"Q: {question}")
            print(f"A: {answer}")
            print()
        return

    if not args.build:
        parser.print_help()


if __name__ == "__main__":
    main()

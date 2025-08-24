# main.py

from memory_engine import save_memory, search_memory
import argparse

def main():
    parser = argparse.ArgumentParser(description="🧠 AI Memory Palace")

    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

    # Save memory
    save_parser = subparsers.add_parser("save", help="Save a memory")
    save_parser.add_argument("thought", type=str, help="The thought or idea to save")

    # Search memory
    search_parser = subparsers.add_parser("search", help="Search memory")
    search_parser.add_argument("query", type=str, help="Query to search in memory")
    search_parser.add_argument("--top_k", type=int, default=3, help="Number of results to show")
    search_parser.add_argument("--summarize", action="store_true", help="Summarize results using GPT")

    args = parser.parse_args()

    if args.command == "save":
        save_memory(args.thought)
    elif args.command == "search":
        search_memory(args.query, top_k=args.top_k, summarize=args.summarize)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

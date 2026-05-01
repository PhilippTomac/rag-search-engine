import argparse
from lib.keyword_search import search_command

def main() -> none:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparser = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparser.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            #Print the search query
            print("Searching for:", args.query)
            results = search_command(args.query)
            for i, result in enumerate(results, 1):
                print(f"{i}. {result['title']}")
        case _:
            parser.print_help()

if __name__ == "__main__":
    main()


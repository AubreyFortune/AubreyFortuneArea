"""Command-line entry point."""

import argparse


def greeting(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to AubreyFortuneArea."


def main() -> None:
    parser = argparse.ArgumentParser(description="AubreyFortuneArea demo CLI")
    parser.add_argument("name", nargs="?", default="world", help="name to greet")
    args = parser.parse_args()
    print(greeting(args.name))


if __name__ == "__main__":
    main()

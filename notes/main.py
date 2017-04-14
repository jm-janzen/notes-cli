import sys
import os

from core.cli import CLI
from core.config import Config
from core.book.book import Book

def main():
    """ Package/CLI entry point """

    # Validate config.cfg, init Config singleton
    try:
        Config(os.path.join("notes", "config.cfg"))

    # If failure in configuration, don't even
    except Exception as e:
        print(f"Error reading config.cfg:\n{e}")
        exit(1)

    # Validate items in notes directory, init Book singleton
    try:
        Book()

    except Exception as e:
        print(f"Error building notes dir:\n{e}")
        exit(1)

    # Pass args to our CLI module and execute
    try:
        CLI(sys.argv)

    except Exception as e:
        print(f"Error executing command:\n{e}")

main()

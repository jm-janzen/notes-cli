import sys
import os

from core.cli import CLI
from core.config import Config
from core.book.book import Book

def main():
    """ Package/CLI entry point """

    # Init, validate configuration
    try:
        config = Config(os.path.join("notes", "config.cfg"))

    # If failure in configuration, don't even
    except Exception as e:
        print(f"ERROR: {e}")
        exit(1)

    #
    # TODO try build notes obj here before continuing
    #
    #try:
    #    book = Book()
    #except Exception as e:
    #    print(f"ERROR: {e}\n")
    #    exit(1)
    book = Book()

    # Init CLI
    cli = CLI(sys.argv)

main()

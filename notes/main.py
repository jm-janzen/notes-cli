import sys
import os

from core.cli import CLI
from core.config import Config

def main():
    """ Package/CLI entry point """

    # Init, validate configuration
    config = Config(os.path.join("notes", "config.cfg"))

    # Init CLI
    cli = CLI(sys.argv)

main()

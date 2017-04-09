import argparse
import sys

from .command_ctl import CommandCtl

class CLI:
    def __init__(self, argv):
        """ Parse, Validate, Execute argument(s)
        :param argv: argument(s) to act upon
        """

        args = self._parse_args(argv)
        args = self._trim_args(args)

        command_ctl = CommandCtl()
        command_ctl.run(args)


    def _trim_args(self, args):
        """ Take argparse namespace and rm untrue args
        :param args: namespace obj to trim
        :return args: just the remaining dict
        """

        # Collect attributes for deletion
        rm_me = []
        for k, v in args.__dict__.items():
            if v is False or v is None:
                rm_me.append(k)

        # Delete them
        for rm in rm_me:
            delattr(args, rm)

        return args.__dict__


    def _parse_args(self, argv):
        """ Parse and Validate arguments
        :param argv: argument(s) from init
        :return args: parsed, validated argument(s)

        TODO replace "help" here with samesuch method of command

        """
        parser = argparse.ArgumentParser()

        parser.add_argument("-e", "--edit",
                            help="edit given item (topic)",
                            type=str,
                            nargs='+')
        parser.add_argument("-l", "--list",
                            help="list all notes",
                            action="store_true")
        parser.add_argument("-L", "--long-list",
                            help="list all notes, with more detail",
                            action="store_true")

        # FIXME consider making these switches to --list arg instead of their own thing
        parser.add_argument("-T", "--topic-list",
                            help="list all topics",
                            action="store_true")
        parser.add_argument("-S", "--subject-list",
                            help="list all subjects",
                            action="store_true")

        # If no arguments, just print usage and exit
        if len(argv) <= 1:
            parser.print_help()
            parser.exit()

        return parser.parse_args()


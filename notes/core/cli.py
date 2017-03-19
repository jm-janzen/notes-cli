import argparse

from .command_ctl import CommandCtl

class CLI:
    def __init__(self, argv):
        """ Parse, Validate, Execute argument(s)
        :param argv: argument(s) to act upon
        """

        args = self.parse_args(argv)

        command_ctl = CommandCtl()
        command_ctl.execute(self.arg_to_str(args))

    def arg_to_str(self, args):
        if args.list:
            return "list"

    def parse_args(self, argv):  # XXX argv not nessa  :/
        """ Parse and Validate arguments
        :param argv: argument(s) from init
        :return args: parsed, validated argument(s)
        """
        parser = argparse.ArgumentParser()

        parser.add_argument("-l", "--list",
                            help="list all notes",
                            action="store_true")

        return parser.parse_args()


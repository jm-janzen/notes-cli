import argparse
import sys

from .command_ctl import CommandCtl

class CLI:
    def __init__(self, argv):
        """ Parse, Validate, Execute argument(s)
        :param argv: argument(s) to act upon
        """

        print("A:",argv)
        args = self._parse_args(argv)
        print("B:",args)

        command_ctl = CommandCtl()
        command_ctl.execute(self._arg_to_str(args))

    def _arg_to_str(self, arg):
        """ Get string representation of argument,
        i.e. "args.list" will return "list"
        :param arg: single argparse.Namespace obj
        :return arg: string name of obj

        FIXME this is probably dumb, and should be replaced
              elsewhere with if-elif structure.

        """
        # Iterate over key=name, val=bool
        for key, val in list(vars(arg).items()):

            print(key, val)

            # Check if singular arg is just a flag and return first on
            if type(val) is bool:
                if val:
                    return key

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
                            nargs=1)
        parser.add_argument("-l", "--list",
                            help="list all notes",
                            action="store_true")
        parser.add_argument("-L", "--long-list",
                            help="[UNIMPLEMENTED] list all notes, with more detail",
                            action="store_true")
        parser.add_argument("-T", "--topic-list",
                            help="[UNIMPLEMENTED] list all topics",
                            action="store_true")
        parser.add_argument("-S", "--subject-list",
                            help="[UNIMPLEMENTED] list all subjects",
                            action="store_true")

        # If no arguments, just print usage and exit
        if len(argv) <= 1:
            parser.print_help()
            parser.exit()

        return parser.parse_args()


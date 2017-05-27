import argparse
import sys

class CLIBuilder:

    def parse_args(self, argv):
        args = self._parse_args(argv)
        args = self._trim_args(args)

        return args

    def _trim_args(self, args):
        """ Take argparse namespace and rm untrue args
        :param args: namespace obj to trim
        :return args: just the remaining dict
        """
        #print(f"cli::_trim_args({args})")

        # Collect attributes for deletion
        rm_me = []
        for k, v in args.__dict__.items():

            # rm missing of false flags
            if v is False or v is None:

                # Help & Usage are special case, store None, so preserve
                if not any(k == s for s in [ "help", "usage" ]):
                    rm_me.append(k)

            # rm empty lists (for positional args)
            elif isinstance(v, list):
                if len(v) < 1:
                    rm_me.append(k)

        # Delete them
        for rm in rm_me:
            delattr(args, rm)

        # Strip namespace, ret dict only
        return args.__dict__

    def _parse_args(self, argv):
        """ Parse and Validate arguments
        :param argv: argument(s) from init
        :return args: parsed, validated argument(s)
        """
        #
        #TODO replace "help" here with samesuch method of command
        #

        parser = argparse.ArgumentParser(prog="notes",
                                         usage="%(prog)s [options]",
                                         add_help=False)

        parser.add_argument("-h", "--help",
                            help="print all help, or help for given command",
                            choices=("help", "usage", "view", "find",
                                     "edit", "create", "list"),
                            nargs="?",
                            default=argparse.SUPPRESS)
        parser.add_argument("-u", "--usage",
                            help="print more detailed help for given command",
                            choices=("help", "usage", "view", "find",
                                     "edit", "create", "list"),
                            nargs="?",
                            default=argparse.SUPPRESS)

        parser.add_argument("view",
                            help="view topic using pager in config",
                            metavar="topic_path",
                            type=str,
                            nargs='*')
        parser.add_argument("-f", "--find",
                            help="display topics with given str in them",
                            metavar="search_str",
                            type=str,
                            nargs='+')
        parser.add_argument("-e", "--edit",
                            help="edit given item (topic)",
                            type=str,
                            nargs='+')
        parser.add_argument("-c", "--create",
                            help="create given [subjects...] <topic>",
                            type=str,
                            nargs='+')

        # TODO rewrite so accept N* "filter" opt
        #      Ex: `notes -l 'trouble'`
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
        # TODO replace this with out commands/help.py once stable
        if len(argv) <= 1:
            parser.print_help()
            parser.exit()

        return parser.parse_args()


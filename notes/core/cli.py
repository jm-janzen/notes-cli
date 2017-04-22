import sys

from . cli_builder import CLIBuilder
from . command_ctl import CommandCtl

class CLI:
    def __init__(self, argv):
        """ Parse, Validate, Execute argument(s)
        :param argv: argument(s) to act upon
        """

        cli_builder = CLIBuilder()
        args = cli_builder.parse_args(argv)

        # FIXME might be better to pass method={execute, help, usage} here,
        #       and make CLIBuilder entirely responsible for formatting this.

        command_ctl = CommandCtl()
        command_ctl.run(args)


import os
import importlib

from . utils import fileops

class CommandCtl:

    # Generic holder for scripts in core/commands dir
    scripts = {}

    def __init__(self):
        """ Init command packages based on individual scripts in core/commands dir """

        # TODO set this globally before getting here
        # Build relative path to commands dir
        command_script_dir = os.path.join(os.path.dirname(__file__), "commands")

        for command_script in os.listdir(command_script_dir):
            command_script_key = command_script.split('.')[0]

            if fileops._is_hidden(command_script):
                continue

            # FIXME gotta be a more elegant way
            self.scripts[command_script_key] = command_script_key


    def run(self, args):
        """ Parse args into (cmd, **args) for _execute """
        cmd, args = self._parse_args(args)

        if cmd == "help":

            # Key of help is actually command, so call _help(args), instead
            # of expected _help(cmd).
            # If args None, this is blank help, so set to that (cmd).
            # XXX this might be a problem if we implement `--usage [cmd]`
            self._help(args or cmd)

        elif cmd == "usage":

            self._usage(args or cmd)

        else:
            self._execute(cmd, args)

    def _parse_args(self, args):
        """ Separate cmd from *args, and ret
        :param args: dict to look in
        :return cmd, args: tuple of command to run & list of extra arguments for command
        """

        return list(args.keys())[0], list(args.values())[0]

    def _usage(self, cmd):
        """ Pass argument to individual handlers
        :param cmd: command/<cmd>.py::usage() to to use

        TODO fix duplicated code with _execute & _help methods below

        """

        # Get str ref to command by name
        c = self.scripts.get(cmd)

        # Import by name at std path
        cmd_module = importlib.import_module(f"core.commands.{c}")

        # By convention, call `execute` method of imported cmd script
        cmd_module.usage()

    def _help(self, cmd):
        """ Pass argument to individual handlers
        :param cmd: command/<cmd>.py::help() to to use

        TODO fix duplicated code with _execute method below

        """

        # Get str ref to command by name
        c = self.scripts.get(cmd)

        # Import by name at std path
        cmd_module = importlib.import_module(f"core.commands.{c}")

        # By convention, call `execute` method of imported cmd script
        cmd_module.help()


    def _execute(self, cmd, args):
        """ Pass argument to individual handlers
        :param cmd: command/<cmd>.py to to use
        :param args: extra arguments to pass to command - either list, or bool
        """

        # Get str ref to command by name
        c = self.scripts.get(cmd)

        # Import by name at std path
        cmd_module = importlib.import_module(f"core.commands.{c}")

        # By convention, call `execute` method of imported cmd script
        cmd_module.execute(args)


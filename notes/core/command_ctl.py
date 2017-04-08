import os
import importlib

class CommandCtl:

    # Generic holder for scripts in core/commands dir
    scripts = {}

    def __init__(self):
        """ Init command packages based on individual scripts in core/commands dir """

        # TODO set this globally before getting here
        command_script_dir = os.path.join("notes", "core", "commands")

        for command_script in os.listdir(command_script_dir):
            command_script_key = command_script.split('.')[0]

            # FIXME gotta be a more elegant way
            self.scripts[command_script_key] = command_script_key

    def run(self, args):
        """ TODO parse args into (cmd, **args) for _execute """
        print(f"CommandCtl::run({args})")
        cmd, args = self._parse_args(args)

        self._execute(cmd, args)

    def _parse_args(self, args):
        """ TODO separate cmd from *args, and ret """
        print(f"CommandCtl::_parse_args({args})")
        
        cmd, args = list(args.keys())[0], list(args.values())[0]

        return cmd, args

    def _execute(self, cmd, *args):
        """ Pass argument to individual handlers

        TODO handle multiple arguments, and positional arguments
             which should be passed to individual commands. Eg:
             `notes --edit linux arch`.

        """
        print(f"CommandCtl::_execute({cmd}, {args})")

        # Get str ref to command by name
        c = self.scripts.get(cmd)

        # Import by name at std path
        cmd_module = importlib.import_module(f"core.commands.{c}")

        # By convention, call `execute` method of imported cmd script
        cmd_module.execute()

    def get_script(self, name):
        """ Get script ref of a certain name
        :param name: key
        :return scripts[name]: value

        FIXME this is presently unused

        """
        return scripts[name]
    

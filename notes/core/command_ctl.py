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

    def execute(self, cmd):
        """ Pass argument to individual handlers

        XXX BUG this is receiving 'list' on no args from CLI

        """
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
        """
        return scripts[name]
    

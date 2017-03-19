import os
import importlib

from .commands import *

class CommandCtl:

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
        """ Pass argument to individual handlers """

        c = self.scripts.get(cmd)
        cmd_module = importlib.import_module(f"core.commands.{c}")
        cmd_module.execute()

    def get_script(self, name):
        """ Get script ref of a certain name
        :param name: key
        :return scripts[name]: value
        """
        return scripts[name]

    

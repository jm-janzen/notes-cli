import os

from configparser import ConfigParser
from . utils.singleton import Singleton


class Config(metaclass=Singleton):

    def __init__(self, path):
        """ Build config from given file at path """
        self.opts = self._build(path)

    def _build(self, path):
        """ Using config at path, build config singleton

        TODO either move build validation here, or rm this middleman func.

        """
        return self._read_in(path)

    def _read_in(self, path):
        """ Read in config at path and ret basic config object """
        # Prime configuration parser
        cp = ConfigParser()
        cp.read(path)

        # Get abs path to notes dir
        notes_dir = os.path.abspath(os.path.expanduser(cp.get("Paths", "NotesDir")))

        # Get preferred interfaces for viewing/editing topics
        editor = cp.get("Interfaces", "Editor")
        viewer = cp.get("Interfaces", "Viewer")

        # Get accepted topic extensions
        topic_exts = list(map(str.strip, cp.get("TopicPrefs", "Extensions").split(',')))

        # Bundle all in obj and ret
        return {
            "notes_dir": notes_dir,
            "editor": editor,
            "viewer": viewer,
            "prefs": {
                "topic": {
                    "extensions": topic_exts,
                    "ignore_pats": "",
                },
                "subject": {
                    "ignore_pats": "",
                }
            }
        }

    def write_out(self, path, opts):
        """ TODO Write out a new config file at path, using given opts """
        raise Exception("UNIMPLEMENTED")


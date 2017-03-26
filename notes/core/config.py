import os

from configparser import ConfigParser
from . utils.singleton import Singleton


class Config(metaclass=Singleton):

    def __init__(self, path):
        """ Build config from given file at path """
        self.opts = self._build(path)

    def _build(self, path):
        """ Using config at path, build config singleton """
        # Get temporary configuration obj for validation
        c = self._read_in(path)

        # Check notes dir exists
        if not os.path.isdir(c["notes_dir"]):
            raise FileNotFoundError(f"{c['notes_dir']} is not a directory")

        # Check editor exists
        if not os.path.isfile(c["editor"]):
            raise FileNotFoundError(f"{c['editor']} is not a file")

        # Check editor is set as executable
        if not os.access(c["editor"], os.X_OK):
            raise Exception(f"{c['editor']} is not executable")

        # Check viewer exists
        if not os.path.isfile(c["viewer"]):
            raise FileNotFoundError(f"{c['viewer']} is not a file")

        # Check viewer is set as executable
        if not os.access(c["viewer"], os.X_OK):
            raise Exception(f"{c['viewer']} is not executable")

        # TODO validate regex ignore patterns

        # Return fully validated configuration
        return c

    def _read_in(self, path):
        """ Read in config at path and ret basic config object """
        # Prime configuration parser
        cp = ConfigParser()
        cp.read(path)

        # Get abs path to notes dir
        notes_dir = os.path.abspath(os.path.expanduser(cp.get("Paths", "NotesDir")))

        # Get preferred interfaces for viewing/editing topics
        editor = cp.get("Interfaces", "Editor")
        viewer = cp.get("Interfaces", "Viewer")  # Ie. pager

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


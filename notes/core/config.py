import os
import re

from configparser import ConfigParser
from . utils.singleton import Singleton

#
# TODO allow passing of new config (for testing)
#

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

            # Prompt for input (maybe user has not setup a notes dir)
            if input(f'{c["notes_dir"]} not found - create it? [y|N]: ').upper() == 'Y':
                self._create_notes_dir(c["notes_dir"])

            # Or just crash, and let user handle this in their OS
            else:
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
        # Build relative path to named config file
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, path))

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
        new_topic_ext = cp.get("TopicPrefs", "NewTopicExtension")

        # Get topic, subject patterns to filter by
        topic_ignore_pats = []
        for pat in list(map(str.strip, cp.get("TopicPrefs", "IgnorePatterns").split(','))):
            topic_ignore_pats.append(re.compile(pat))
        subject_ignore_pats = []
        for pat in list(map(str.strip, cp.get("SubjectPrefs", "IgnorePatterns").split(','))):
            subject_ignore_pats.append(re.compile(pat))

        # Bundle all in obj and ret
        return {
            "notes_dir": notes_dir,
            "editor": editor,
            "viewer": viewer,
            "prefs": {
                "topic": {
                    "extensions": topic_exts,
                    "new_topic_ext": new_topic_ext,
                    "ignore_pats": topic_ignore_pats,
                },
                "subject": {
                    "ignore_pats": subject_ignore_pats,
                }
            }
        }

    def _create_notes_dir(self, path):
        """ Create an empty notes dir at given path """
        os.makedirs(path)
        print(f"Created new (empty) notes dir: \"{path}\"")

    def topic_extensions_pat(self):
        """ Return regex pattern matching any acceptable topic file extension """
        return re.compile('|'.join(self.opts["prefs"]["topic"]["extensions"]))

    def new_config(self, new_path):
        """ TODO use file at new path as new configuration """
        pass

    def write_out(self, path, opts):
        """ TODO Write out a new config file at path, using given opts """
        raise Exception("UNIMPLEMENTED")


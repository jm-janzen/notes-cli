import os

from .. config import Config
from .. utils import fileops
from . topic import Topic


class Subject():
    """
    TODO update this doc
    Subject = {
        linux: {
            parent_subject: notes,
            child_topics:   [ arch ... ],
            child_subjects: [ desktop ... ],
            path:           ~/notes/linux,
            name:           linux,
        }
    }
    """

    def __init__(self, path):
        """ Build subject obj from full path """
        #print(f"new Subject({path})")

        subj_arr = path.split(os.sep)

        # Set class properties
        self.path     = path
        self.name     = subj_arr[-1]
        self.parent   = subj_arr[-2]
        self.children = {
            "topics": self._build_topics(path),  # FIXME make "push" method and add from book_builder
                                                 # then will only need to check for hidden, pats once
            "subjects": self._build_subjects(path),
        }

    def _build_topics(self, path):
        """ Return list of topics in subject """
        files = []
        for file in os.listdir(path):

            file_path = os.path.join(path, file)

            if fileops._is_hidden(file):
                continue

            if os.path.isfile(file_path):
                files.append(Topic(file_path))

        return files


    def _build_subjects(self, path):
        """ Return list of subjects in subject """
        dirs = []
        for file in os.listdir(path):

            file_path = os.path.join(path, file)

            if fileops._is_hidden(file):
                continue

            if os.path.isdir(file_path):
                dirs.append(Subject(file_path))

        return dirs


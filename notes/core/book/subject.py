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

        subj_arr = path.split(os.sep)

        # Set class properties
        self.path     = path
        self.name     = subj_arr[-1]
        self.parent   = subj_arr[-2]
        self.children = {
            "topics": [],  # Populated using method add_topic
            "subjects": self._build_subjects(path),
        }


    def add_topic(self, path):
        """ Given path to file, add instance of Topic to this Subject """
        # XXX if new instance does not quack, it is of no use to us
        new_topic = Topic(path)
        if new_topic.quack:
            self.children["topics"].append(new_topic)


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


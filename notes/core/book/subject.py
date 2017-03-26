import os

from .. config import Config
from .. utils import fileops
from . topic import Topic


class Subject():
    """
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

    #def __init__(self, path):
    def __init__(self, path, topic_paths):
        """ Build subject obj from full path

        TODO recursively build subjects, topics

        """
        print(f"new Subject({path}, {topic_paths})")

        # TODO replace all these with os.sep
        subj_arr = path.split('/')

        # Set class properties
        self.path     = path
        self.name     = subj_arr[-1]
        self.parent   = subj_arr[-2]
        self.children = {
            "topics": topic_paths,
            "subjects": self._build_subjects(path),
        }

        # XXX populating children from os.walk files
        """
        self.children = {"topics": []}
        for topic_path in topic_paths:
            self.children["topics"].append(Topic(topic_path))
        """

    def _build_topics(self, path):
        """ TODO return list of topics in subject """
        files = []
        for file in os.listdir(path):

            file_path = os.path.join(path, file)

            if fileops._is_hidden(file):
                continue

            if os.path.isfile(file_path):
                files.append(Topic(file_path))

        return files

    def _build_subjects(self, path):
        """ TODO return list of subjects in subject """
        dirs = []
        for file in os.listdir(path):

            file_path = os.path.join(path, file)

            if fileops._is_hidden(file):
                continue

            if os.path.isdir(file_path):
                dirs.append(Subject(file_path, os.listdir(file_path)))

        return dirs


import os
from configparser import ConfigParser

from . subject import Subject
from . topic import Topic
from .. utils import fileops
from .. config import Config

class BookBuilder():
    """ Build and return book obj containing Subjects, Topics

    NOTE most validation done in Subject, Topic ctors.

    """

    book = {
            "index": {  # Special "root" subject
                "subjects": [],
                "topics": [],
                },
            }

    def __init__(self):
        """ Using config, build book object from notes dir """

        # Fetch notes dir from singleton
        config    = Config()
        notes_dir = config.opts["notes_dir"]

        # Fetch ignore pats for filtering
        self.ignore_topics   = config.opts["prefs"]["topic"]["ignore_pats"]
        self.ignore_subjects = config.opts["prefs"]["subject"]["ignore_pats"]

        for curr, dirs, files in os.walk(notes_dir):

            # Skip all if we're in a hidden path
            if fileops._is_hidden(curr):
                continue

            # Skip ignored Subject dirs onward
            if self._is_ignored_subject(curr):
                continue

            # Build Subject for Book
            subject_cls = Subject(curr)

            # Append files here to Subject's child Topics
            for file in files:

                # Skip ignored Topics
                if self._is_ignored_topic(file):
                    continue

                subject_cls.add_topic(os.path.join(curr, file))

                # While here, append topics to flat list in index
                topic_cls = Topic(os.path.join(curr, file))
                if topic_cls.quack:
                    self.book["index"]["topics"].append(topic_cls)

            # Append Subject class obj to Book
            self.book["index"]["subjects"].append(subject_cls)

    def _is_ignored_topic(self, s):
        """ Return whether Topic should be ignored """
        return self._is_ignored_generic(s, self.ignore_topics)

    def _is_ignored_subject(self, s):
        """ Return whether Subject should be ignored """
        return self._is_ignored_generic(s, self.ignore_subjects)

    def _is_ignored_generic(self, s, pats):
        """ Return whether given str is in given regex pats

        TODO this could probably be simplified

        """
        match = False
        for item in s.split(os.sep):
            if any(pat.findall(item) for pat in pats):
                ignore = True
        return match

    def new_book(self):
        return self.book


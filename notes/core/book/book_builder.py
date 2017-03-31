import os
from configparser import ConfigParser

from . subject import Subject
from . topic import Topic
from .. config import Config

class BookBuilder():
    """ TODO build and return book obj Subjects, Topics """

    book = {
            "index": {  # Special "root" subject
                "subjects": [],
                "topics": [],
                },
            }


    def __init__(self):
        """ TODO using config, build book object from notes dir
        2 stage process:
            - 1. Build "index" of all subjects, topics, with no relations
            - 2. Above iters over files, dirs - building associated Topics, Subjects
                 as appropriate.
        """

        # Fetch notes dir from singleton
        config    = Config()
        notes_dir = config.opts["notes_dir"]
        topic_exts= config.opts["prefs"]["topic"]["extensions"]

        #
        # Step 1. Build flat "index"
        #

        for curr, dirs, files in os.walk(notes_dir):

            # Skip all if we're in a hidden path
            if self._is_hidden(curr):
                continue

            # Build Subject for Book
            subject_cls = Subject(curr)

            # Append files here to Subject's child Topics
            for file in files:
                subject_cls.add_topic(os.path.join(curr, file))

            # Append Subject to Book
            self.book["index"]["subjects"].append(subject_cls)

        """ TODO push topics to individual subjects here, rather than having Subject do it
        for curr, dirs, topics in os.walk(notes_dir):
            for topic in topics:
                topic_arr = topic.split('.')

                # Skip unparsable files
                if len(topic_arr) != 2:
                    continue

                # Skip files not in config ext whitelist
                if not topic_arr[-1] in topic_exts:
                    continue

                if self._is_hidden(topic):
                    continue

                topic_name, topic_ext = topic_arr
            """


    def new_book(self):
        return self.book


    def _is_hidden(self, path):
        """ Check if any part of a std path str starts with hidden token
        :param path: some valid path str
        :return Boolean: whether anything is hidden in path

        FIXME remove this, and use module in utils

        """
        return any(p.startswith('.') for p in path.split('/'))


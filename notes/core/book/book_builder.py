import os
from configparser import ConfigParser

from . subject import Subject
from . topic import Topic
from .. config import Config

class BookBuilder():
    """ TODO build and return book obj Subjects, Topics """

    # TODO populate
    book = { "subjects": [] }

    def __init__(self):
        """ TODO using config, build book object from notes dir """

        # Fetch notes dir from singleton
        config    = Config()
        notes_dir = config.opts["notes_dir"]
        topic_exts= config.opts["prefs"]["topic"]["extensions"]

        # FIXME maybe better idea to build notes (subject, topics) objects elsewhere,
        # since it is fundamental to this package.
        for curr, dirs, topics in os.walk(notes_dir):

            # Skip all if we're in a hidden path
            if self._is_hidden(curr):
                continue

            depth = len(curr.split(os.sep)) - len(notes_dir.split(os.sep))
            print(depth, curr)

            # Get name of current dir
            #self.book["subjects"].append(Subject(curr)) # FIXME maybe pass topics[] in here
            topic_obj_arr = []
            for topic in topics:
                topic_obj_arr.append(Topic(os.path.join(curr, topic)))
            self.book["subjects"].append(Subject(curr, topic_obj_arr)) # FIXME maybe pass topics[] in here

            """
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


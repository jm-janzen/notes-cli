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
                },
            }

    def __init__(self):
        """ Using config, build book object from notes dir """

        # Fetch notes dir from singleton
        config    = Config()
        notes_dir = config.opts["notes_dir"]

        for curr, dirs, files in os.walk(notes_dir):

            # Skip all if we're in a hidden path
            if fileops._is_hidden(curr):
                continue

            # Build Subject for Book
            subject_cls = Subject(curr)

            # Append files here to Subject's child Topics
            for file in files:
                subject_cls.add_topic(os.path.join(curr, file))

            # Append Subject class obj to Book
            self.book["index"]["subjects"].append(subject_cls)


    def new_book(self):
        return self.book


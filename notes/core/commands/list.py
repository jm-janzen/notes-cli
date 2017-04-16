import os

from .. config import Config
from .. book.book import Book

# Fetch notes dir from singleton
config    = Config()
notes_dir = config.opts["notes_dir"]

def execute(args):
    """ Print notes' subjects, topics """

    book    = Book()
    prt_str = ''

    for subject in book.index["subjects"]:

        # Prepend Subject's parents
        for parent in book.get_parents(subject):
            prt_str += f"{parent.name}."

        prt_str += f"{subject.name}\n"

        for topic in subject.children["topics"]:

            prt_str += f"  {topic.name}\n"

    print(prt_str, end='')

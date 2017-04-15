import os

from .. config import Config
from .. book.book import Book

# Fetch notes dir from singleton
config    = Config()
notes_dir = config.opts["notes_dir"]

def execute(args):
    """ Print notes' subjects, topics """

    prt_str = ''

    for subject in Book().index["subjects"]:

        prt_str += f"{subject.name}\n"

        for topic in subject.children["topics"]:

            prt_str += f"  {topic.name}\n"

    print(prt_str, end='')

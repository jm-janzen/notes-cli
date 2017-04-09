import os

from .. book.book import Book

def execute(args):
    """ Print flat list of all topics """
    prt_str = ''
    for subject in Book()["index"]["subjects"]:

        for topic in subject.children["topics"]:
            prt_str += topic.name + '\n'

    # Print topics, minus extra trailing newline
    print(prt_str[:-1])


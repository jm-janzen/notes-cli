import os

from .. book.book import Book

def execute():
    """ Print flat list of all topics """
    prt_str = ''
    for subject in Book()["index"]["subjects"]:

        for topic in subject.children["topics"]:
            prt_str += '\n' + topic.name

    print(prt_str)


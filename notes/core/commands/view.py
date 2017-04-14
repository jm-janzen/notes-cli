import os
import subprocess  # For viewing topic file

from .. book.book import Book
from .. config import Config

# Fetch notes dir from singleton
config    = Config()
notes_dir = config.opts["notes_dir"]
topic_exts= config.opts["prefs"]["topic"]["extensions"]


def execute(args):
    """ Look for [subject] <topic> and view """
    #print(f"view::execute({args})")

    try_name = args[-1]
    try_dir  = os.path.join(notes_dir, *args[:-1])
    try_path = os.path.join(notes_dir, *args)

    # Throw up, if this is not a valid subject dir
    if not os.path.isdir(try_dir):
        raise FileNotFoundError(f"{try_dir} is not a subject/directory")

    #
    # FIXME use get_topic method, rather than iter
    #
    found_file = None
    for subject in Book().index["subjects"]:

        for topic in subject.children["topics"]:
            if not topic.name == try_name:
                continue

            # Open file for editing, and quit
            found_file = topic.path

    if found_file is None:

        print(f"Could not find topic file matching {try_path}.*")

    else:

        _view_file(found_file)


def _view_file(f):
    """ View file at given path using pager in config.cfg """
    #print(f"view::_view_file({f})")

    subprocess.call([config.opts["viewer"], f])


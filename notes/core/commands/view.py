import os
import subprocess  # For viewing topic file

from .. book.book import Book
from .. config import Config

# Fetch notes dir from singleton
config    = Config()
notes_dir = config.opts["notes_dir"]


def execute(args):
    """ Look for [subject] <topic> and view """
    #print(f"view::execute({args})")

    # FIXME rm these if not nessa
    try_name = args[-1]
    try_dir  = os.path.join(notes_dir, *args[:-1])
    try_path = os.path.join(notes_dir, *args)

    # Throw up, if this is not a valid subject dir
    if not os.path.isdir(try_dir):
        raise FileNotFoundError(f"{try_dir} is not a subject/directory")

    found_file = Book().get_topic(args)

    if found_file is None:

        print(f"Could not find topic file matching {try_path}.*")

    else:

        _view_file(found_file.path)


def help():

    print("""topic_path            view topic using pager in config""")


def _view_file(f):
    """ View file at given path using pager in config.cfg """
    #print(f"view::_view_file({f})")

    subprocess.call([config.opts["viewer"], f])


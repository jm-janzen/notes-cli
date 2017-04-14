import os
import tempfile    # For creating temp file
import subprocess  # For editing  temp file
import shutil      # For copying  temp file over original

from .. book.book import Book
from .. config import Config

# Fetch notes dir from singleton
config    = Config()
notes_dir = config.opts["notes_dir"]
new_topic_ext = config.opts["prefs"]["topic"]["new_topic_ext"]

def execute(args):
    """ Create [SUBJECTS...] <TOPIC> specified, if not found """
    #print(f"create::execute({type(args)} {args})")

    try_name = args[-1]
    try_dir  = os.path.join(notes_dir, *args[:-1])
    try_path = os.path.join(notes_dir, *args)

    #
    # FIXME use get_topic method, rather than iter
    #
    found_file = None
    for subject in Book().index["subjects"]:

        # Check if topic file already exists
        # FIXME will collide if another topic _anywhere_ of same name
        for topic in subject.children["topics"]:
            if not topic.name == try_name:
                continue

            found_file = topic.path

    if found_file is not None:
        print(f"Topic file of the same name already exists at {try_path}.*")
        exit(1)

    # Create subject dirs if not exists
    if not os.path.isdir(try_dir):
        os.makedirs(try_dir)
        print(f"Created subject dir(s) {try_dir}")

    # Create topic file
    open(os.path.join(try_path + new_topic_ext), 'a').close()
    print(f"Created topic file {try_path}{new_topic_ext}")


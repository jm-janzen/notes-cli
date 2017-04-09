import re
import subprocess  # For viewing topic file(s)

from .. book.book import Book
from .. config import Config

# Fetch notes dir from singleton
config = Config()

def execute(args):
    """ Find matches in existing topics """
    #print(f"find::execute({args})")

    # Collect any multiples, and interpret as OR
    search_str = '|'.join(args)

    matching_topics = []
    for topic in Book()["index"]["topics"]:
        with open(topic.path) as tp:
            contents = tp.read()

        if re.search(search_str, contents):

            # Collect matching topics
            matching_topics.append(topic)

    if len(matching_topics) < 1:
        print(f"Could not find any topics containing '{search_str}'")

    else:

        # Splat matching pats into pager
        # FIXME `--pattern` arg will only work with less
        subprocess.run([config.opts["viewer"],
                        "--pattern="+search_str,
                        *(m.path for m in matching_topics)])


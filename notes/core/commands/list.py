import os
import termcolor

from .. config import Config

def execute():
    """ Print notes subjects, topics """

    # Fetch notes dir from singleton
    config    = Config()
    notes_dir = config.opts["notes_dir"]
    topic_exts= config.opts["prefs"]["topic"]["extensions"]

    # FIXME maybe better idea to build notes (subject, topics) objects elsewhere,
    # since it is fundamental to this package.
    for curr, dirs, topics in os.walk(notes_dir):

        # Skip all if we're in a hidden path
        if _is_hidden(curr):
            continue

        # Get name of current dir
        subject = curr.split('/')[-1]

        print(termcolor.colored(subject.upper(), "blue"))

        for topic in topics:
            topic_arr = topic.split('.')

            # Skip unparsable files
            if len(topic_arr) != 2:
                continue

            # Skip files not in config ext whitelist
            if not topic_arr[-1] in topic_exts:
                continue

            if _is_hidden(topic):
                continue

            topic_name, topic_ext = topic_arr

            print('  ' + topic_name)


def _is_hidden(path):
    """ Check if any part of a std path str starts with hidden token
    :param path: some valid path str
    :return Boolean: whether anything is hidden in path
    """
    return any(p.startswith('.') for p in path.split('/'))

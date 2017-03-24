import os
import termcolor


def execute():
    """ Print notes subjects, topics """

    # TODO determine this globally before getting here
    notes_dir = os.path.join(os.path.expanduser('~'),
                             "notes")

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

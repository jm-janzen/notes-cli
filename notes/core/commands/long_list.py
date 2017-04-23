import os
import time

from .. book.book import Book

def execute(args):
    """ Print associated list of subjects and their topics """
    for subject in Book().index["subjects"]:

        # Determine whether to print subject's parent-subject, and fmt appropriately
        # FIXME notes_dir not in `~` will falsely indicate big depth numbers
        # FIXME handle subjects' whose parents have parents other than root notes_dir
        # FIXME this is duplicated from subject_list command
        depth = len(subject.path.split(os.sep))

        if depth > 5:
            prt_str = f"{subject.parent}.{subject.name}"
        else:
            prt_str = subject.name

        # Add children num
        prt_str += f" ({len(subject.children['topics'])})"


        for topic in subject.children["topics"]:
            time_str = time.strftime('%m-%d-%Y', time.gmtime(os.path.getmtime(topic.path)))
            prt_str += f"\n  {topic.name} ({time_str})"

        print(prt_str)


def help():
    print("""-L, --long-list       list all notes, with more detail""")


def usage():
    print("TODO")


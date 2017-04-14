import os

from .. book.book import Book

def execute(args):
    """ Print flat list of all subjects """
    for subject in Book().index["subjects"]:

        # Determine whether to print subject's parent-subject, and fmt appropriately
        # FIXME notes_dir not in `~` will falsely indicate big depth numbers
        # FIXME handle subjects' whose parents have parents other than root notes_dir
        depth = len(subject.path.split(os.sep))
        
        if depth > 5:
            prt_str = f"{subject.parent}.{subject.name}"
        else:
            prt_str = subject.name

        print(prt_str)

import termcolor

from .. book.book import Book

def execute():
    book = Book()
    for subjects in book.values():
        for subject in subjects:
            pass


            """
            depth = 0
            for key, child in subject.children.items():
                #print(depth, key, child)
                for baby in child:
                    print(depth, key, baby.name)
                depth += 1
            """


            for s in subject.children["subjects"]:
                print(termcolor.colored(s.name.upper(), "blue"))

            """
            for t in subject.children["topics"]:
                print('  ' + t.name)
            """

def collect_subjects(start, depth=-1):
    subjects = []
    def _recurse(curr, depth):
        if depth != 0:

            for children in start.children.values():
                for child in children:
                    print(curr.name)
                    _recurse(child, depth - 1)

    _recurse(start, depth)

    return subjects

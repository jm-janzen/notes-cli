
def execute(args):
    pass


def help():
    prt_str = """usage: notes [options]

positional arguments:
  topic_path            view topic using pager in config

optional arguments:
  -h [HELP], --help [HELP]
                        view topic using pager in config
  -f search_str [search_str ...], --find search_str [search_str ...]
                        display topics with given str in them
  -e EDIT [EDIT ...], --edit EDIT [EDIT ...]
                        edit given item (topic)
  -c CREATE [CREATE ...], --create CREATE [CREATE ...]
                        create given [subjects...] <topic>
  -l, --list            list all notes
  -L, --long-list       list all notes, with more detail
  -T, --topic-list      list all topics
  -S, --subject-list    list all subjects"""

    print(prt_str)

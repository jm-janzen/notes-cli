import os

from .. utils.singleton import Singleton
from .. config import Config
from . book_builder import BookBuilder


class Book(metaclass=Singleton):
    """ Interface to book obj (notes dir)
    Example obj fmt:
        Book = {
            index: {
                topics:  [ arch ... ],
                subjects: [ linux ... ],
            },
        }
        Subject = {
            linux: {
                parent_subject: notes,
                child_topics:   [ arch ... ],
                path:           ~/notes/linux,
                name:           linux,
            }
        }

        Topic = {
            arch: {
                parent_subject: linux,
                path:           ~/notes/linux/arch.mkd,
                ext:            mkd,
                name:           arch,
            }
        }
    """

    def __init__(self):
        """ Set property book index """
        self.__index = BookBuilder().new_book()["index"]

    @property
    def index(self):
        """ Return index of book singleton dict """
        return self.__index

    def get_topic(self, path):
        """ Return Topic obj at given path list
        :param path: list [SUBJECT...] <TOPIC>
        :return Topic: Topic matching given Subject-path, Topic-name
        """
        #print(f"Book::get_topic({path})")

        # Trim topic from end
        topc_name = path[-1]

        # If multiple elems, get subject to iter over child topics
        subj_obj = None
        if len(path) > 1:
            subj_obj = self.get_subject(path[0:len(path)+1][-2])

        # Get list of topics for final op
        if subj_obj is None:  # Just look in index
            topc_objs = self.__index["topics"]
        else:  # Look in Subject's child topics
            topc_objs = subj_obj.children["topics"]

        # Build named dict of Topics for get (below)
        d = dict((t.name, t) for t in topc_objs)

        return d.get(topc_name)

    def get_subject(self, subject_name):
        """ Return subject obj at given subject name str
        :param subject_name: str matching a Subject's name
        :return Subject: Subject matching given str

        FIXME What to do with re to duplicate Subject names?

        """
        #print(f"Book::get_subject({subject_name})")

        # Build named dict of Subjects for get (below)
        d = dict((t.name, t) for t in self.__index["subjects"])

        return d.get(subject_name)

    def get_parents(self, item):
        """ Return list of parent subjects, up to notes_dir
        :param item: Subject or Topic, having property `parents`
        :return parents: list of parents from root to item
        """
        #print(f"Book::get_parents({item.name})")

        return reversed(self._recurse_parents(item))

    def _recurse_parents(self, item, parents=[]):
        """ Add to item's parent(s) list
        :param item: Subject or Topic, having property `parents`
        :return parents: list of parents

        Adds item's parent to list, then recurses to check item's
        parent in turn has it's own parent to add, and so on...

        """

        # Make copy, since list type is pass-by-ref otherwise
        parents = parents[:]

        # Done
        if (self._get_depth(item) - 1) <= 0:
            return parents

        # Continue
        else:
            parent_cls = self.get_subject(item.parent)
            parents.append(parent_cls)
            return self._recurse_parents(parent_cls, parents)



    def _get_depth(self, item):
        """ Return int number of dirs from notes_dir """
        #print(f"Book::get_depth({item})")
        root = Config().opts["notes_dir"].count(os.sep)
        end  = item.path.count(os.sep)
        return end - root


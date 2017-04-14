from .. utils.singleton import Singleton
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

    def get_topic(t):
        """ TODO return topic obj at given path obj """
        return t


    def get_subject(s):
        """ TODO return subject obj at given path obj """
        return s


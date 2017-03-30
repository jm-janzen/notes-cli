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

    def __new__(self):
        return BookBuilder().new_book()


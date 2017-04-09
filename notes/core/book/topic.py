from .. config import Config

class Topic():
    """
    Topic = {
        arch: {
            parent_subject: linux,
            path:           ~/notes/linux/arch.mkd,
            name:           arch,
            ext:            mkd,
        }
    }

    TODO Fix newline at the beginning of output

    """

    quack = True

    def __init__(self, path):
        """ Build topic obj from full path

        NOTE if this does not quack, it does not represent
             a useable object.

        """
        #print(f"\tnew Topic({path})")

        # Fetch acceptable extensions from config
        topic_exts= Config().opts["prefs"]["topic"]["extensions"]

        topc_arr = path.split('/')[-2:]
        name_arr  = topc_arr[-1].split('.')

        # Skip unparsable files
        if len(name_arr) != 2:
            self.quack = False

        name = name_arr[0]
        if len(name_arr) > 1:
            ext = name_arr[-1]
        else:
            ext = ''

        # Skip files not in config ext whitelist
        if not ext in topic_exts:
            self.quack = False

        parent = topc_arr[-2]  # subject

        self.path = path
        self.name = name
        self.ext = ext
        self.parent = parent


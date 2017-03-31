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

    def __init__(self, path):
        """ Build topic obj from full path """
        #print(f"new Topic({path})")

        # Fetch acceptable extensions from config
        topic_exts= Config().opts["prefs"]["topic"]["extensions"]

        topc_arr = path.split('/')[-2:]
        name_arr  = topc_arr[-1].split('.')

        # Skip unparsable files
        if len(name_arr) != 2:
            # FIXME include option/instruction to add to config ignore list
            raise Exception(f"Could not build new Topic using {path}")

        path = path
        name = name_arr[0]
        if len(name_arr) > 1:
            ext = name_arr[-1]
        else:
            ext = ''

        # Skip files not in config ext whitelist
        if not ext in topic_exts:
            raise Exception(f"Skipping Topic {path} because extension is being ignored")

        parent = topc_arr[-2]  # subject

        self.path = path
        self.name = name
        self.ext = ext
        self.parent = parent


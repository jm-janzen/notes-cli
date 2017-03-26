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
    """

    def __init__(self, path):
        """ TODO Build topic obj from full path """
        print(f"new Topic({path})")

        topc_arr = path.split('/')
        name_arr = topc_arr[-1].split('.')  # XXX will crash on files without .

        path = path
        name = name_arr[0]
        if len(name_arr) > 1:
            ext = name_arr[-1]
        else:
            ext = ''

        parent = topc_arr[-2]

        self.path = path
        self.name = name
        self.ext = ext
        self.parent = parent


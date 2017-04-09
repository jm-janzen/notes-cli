

def _is_hidden(path):
    """ Check if any part of a std path str starts with hidden token
    :param path: some valid path str
    :return Boolean: whether anything is hidden in path

    TODO rm `_` prefix, this is meant to be exported

    """
    return any(p.startswith('.') or p.startswith('_') for p in path.split('/'))




def _is_hidden(path):
    """ Check if any part of a std path str starts with hidden token
    :param path: some valid path str
    :return Boolean: whether anything is hidden in path
    """
    return any(p.startswith('.') for p in path.split('/'))


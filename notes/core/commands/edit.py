import os
import tempfile
import subprocess

from .. book.book import Book
from .. config import Config

# Fetch notes dir from singleton
config    = Config()
notes_dir = config.opts["notes_dir"]
topic_exts= config.opts["prefs"]["topic"]["extensions"]

def execute(args):
    """ TODO edit given topic file using editor in config.cfg
    for subject in Book()["index"]["subjects"]:

        for topic in subject.children["topics"]:
            pass
    """
    print(f"edit({type(args)} {args})")


    try_name = args[-1]
    try_dir  = os.path.join(notes_dir, *args[:-1])
    try_path = os.path.join(notes_dir, *args)

    # Throw up, if this is not a valid subject dir
    if not os.path.isdir(try_dir):
        raise FileNotFoundError(f"{try_dir} is not a subject/directory")

    exts_pat = config.topic_extensions_pat()

    #
    # FIXME use book, rather than os
    #

    # Look for given file in presumed dir
    found_file = None
    for file in os.listdir(try_dir):

        file_name, file_ext = file.split('.')[0], file.split('.')[-1]

        if not try_name == file_name:
            continue

        if exts_pat.match(file_ext):
            found_file = os.path.join(try_dir, file)

    # TODO create new file instead of printing this message
    if found_file is None:
        print(f"Could not find topic file for {try_path}")

    # Open existing file for editing
    else:
        _open_file(found_file)

def _open_file(f):
    """ TODO open file at path in editor in config
    1) copy existing file to temp file
    2) open this temp file in editor
    3) save updates to temp file over og file

    TODO rename this func, or split it up

    """
    print(f"_open_file({f})")

    #
    # 1) Read in contents of original file
    #

    og_file_contents = b''
    with open(f, 'r') as fp:
        og_file_contents = str.encode(fp.read()) # To bytes

    #
    # 2 Create, open new temp file, with contents of original file
    #

    tmp_file_prefix = f.split('/')[-1].split('.')[0] + '_'
    tmp_file_dir    = os.path.join(os.path.abspath('.'), ".tmp")
    tmp_file_path   = ''

    with tempfile.NamedTemporaryFile(prefix=tmp_file_prefix, suffix=".tmp", dir=tmp_file_dir, delete=False) as tf:
        # Put contents of og file in tmp
        tf.write(og_file_contents)

        tf.seek(0)
        subprocess.call([config.opts["editor"], tf.name])

        tmp_file_path = os.path.join(tmp_file_dir, tmp_file_path)

    #
    # 3) TODO copy edits to original file, and remove temporary file
    # use shutil.copy2 to preserve metadata
    #

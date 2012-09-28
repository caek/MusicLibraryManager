import hashlib
import io

__author__ = 'rlaycock'

class FileStore(object):
    def __init__(self):
        self.file_set = set()

    def Add(self, file_name):
        with io.open(file_name) as f:
            hash = hashlib.md5(f.read())
            if hash not in self.file_set:
                self.file_set.add(hash)

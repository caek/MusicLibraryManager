import hashlib
import io

__author__ = 'rlaycock'

class FileStore(object):
    def __init__(self, duplicateFileHandler, hasher=hashlib.md5):
        self.file_set = set()
        self.hasher = hasher
        self.duplicateFileHandler = duplicateFileHandler

    def Add(self, file_name):
        with io.open(file_name) as f:
            hash = self.hasher(f.read())
            if hash in self.file_set:
                self.duplicateFileHandler(file_name)
            else:
                self.file_set.add(hash)

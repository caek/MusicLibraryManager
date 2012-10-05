import hashlib
import io
import mp3_file

__author__ = 'rlaycock'

class FileStore(object):
    def __init__(self, duplicateFileHandler, hasher=hashlib.md5):
        self.file_dict = {}
        self.hasher = hasher
        self.duplicateFileHandler = duplicateFileHandler

    def Add(self, file_name):
        f = mp3_file.Mp3File(file_name)
        hash = self.hasher(f.data()).digest()
        if hash in self.file_dict:
            self.duplicateFileHandler(file_name)
        else:
            self.file_dict[hash] = file_name

    def EnumerateFiles(self):
        return self.file_dict.values()

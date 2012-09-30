import os

__author__ = 'rlaycock'

def enum_files_in_directory(directory_name):
    for dir_name, file_list, dir_list in os.walk(directory_name):
        for file_name in file_list:
            yield os.path.join(dir_name, file_name)

class DirectoryEnumerator(object):
    def __init__(self, file_handler, file_enumerator=enum_files_in_directory):
        self.file_handler = file_handler
        self.file_enumerator = file_enumerator

    def Enumerate(self, directory_name):
        for file_name in self.file_enumerator(directory_name):
            self.file_handler(file_name)
from __future__ import print_function
from directory_enumerator import DirectoryEnumerator
from file_store import FileStore

__author__ = 'rlaycock'

def main():
    file_handler = FileStore(print)
    directory_enumerator = DirectoryEnumerator(file_handler.Add)

    directory_enumerator.Enumerate(".")

if __name__ == '__main__':
    main()

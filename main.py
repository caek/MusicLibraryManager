import __builtin__
from directory_enumerator import DirectoryEnumerator
from file_store import FileStore

__author__ = 'rlaycock'

def duplicate_file_handler(x):
    print x


def main():
    file_handler = FileStore(duplicate_file_handler)
    directory_enumerator = DirectoryEnumerator(file_handler.Add)

    directory_enumerator.Enumerate(".")

if __name__ == '__main__':
    main()

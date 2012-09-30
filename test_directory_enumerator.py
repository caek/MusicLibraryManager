__author__ = 'rlaycock'

import unittest
import directory_enumerator
from mock import MagicMock, call, patch

class DirectoryEnumeratorTest(unittest.TestCase):
    def test_enumerate_directory(self):
        mockFileHandle = MagicMock()
        mockFileEnumerator = MagicMock(side_effect = [["MyTestDir/MyFile"], None])
        dir_enumerator = directory_enumerator.DirectoryEnumerator(mockFileHandle, mockFileEnumerator)
        dir_enumerator.Enumerate("MyTestDir")

        expectArgsList = [ call("MyTestDir/MyFile")]
        self.assertEqual(mockFileHandle.call_args_list, expectArgsList)

    @patch("os.walk", MagicMock(return_value=[('MyTestDir', [], ['MyFile', ]), ]))
    @patch("os.path.join", MagicMock(side_effect=lambda *x: "/".join(x)))
    def test_default_file_enumerator(self):
        mockFileHandle = MagicMock()
        dir_enumerator = directory_enumerator.DirectoryEnumerator(mockFileHandle)
        dir_enumerator.Enumerate("MyTestDir")

        expectArgsList = [ call("MyTestDir/MyFile")]
        self.assertEqual(mockFileHandle.call_args_list, expectArgsList)

if __name__ == '__main__':
    unittest.main()

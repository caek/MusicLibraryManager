from mock import MagicMock, patch
from main import main

__author__ = 'rlaycock'

import unittest

class MainTest(unittest.TestCase):
    def test_main_calls_enumerator(self):
        with patch("main.DirectoryEnumerator") as dir_enumerator:
            main()

            dir_enumerator.return_value.Enumerate.assert_called_once_with(".")

if __name__ == '__main__':
    unittest.main()

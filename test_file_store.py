import io
import file_store
from mock import MagicMock, patch

__author__ = 'rlaycock'

import unittest

@patch('hashlib.md5', MagicMock(return_value=12345))
@patch('io.open', MagicMock())
class FileStoreTest(unittest.TestCase):
    def setUp(self):
        self.store = file_store.FileStore()

    def test_can_add_file_to_file_store(self):
        self.store.Add("myFile")

        self.assertEqual(self.store.file_set, { 12345 })

    def test_adding_different_file_adds_another_entry_to_the_dictionary(self):
        self.store.Add("myFile")
        with patch('hashlib.md5', MagicMock(return_value=123456)):
            self.store.Add("myOtherFile")

        self.assertEqual(self.store.file_set, { 12345, 123456 })

    def test_adding_two_files_with_different_name_same_content_only_adds_first_file(self):
        self.store.Add("myFile")
        self.store.Add("myFileWithSameContent")

        self.assertEqual(self.store.file_set, { 12345 })

if __name__ == '__main__':
    unittest.main()

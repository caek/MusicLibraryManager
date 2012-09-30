import io
import file_store
from mock import MagicMock, patch

DIFFERENT_HASH_RETURN_VALUE = 123456

HASH_RETURN_VALUE = 12345

HASH_RETURN_VALUE = 12345

__author__ = 'rlaycock'

import unittest

@patch('io.open', MagicMock())
class FileStoreTest(unittest.TestCase):
    def setUp(self):
        self.mockHash = MagicMock()
        self.mockHash.return_value.digest.return_value=HASH_RETURN_VALUE
        self.mockHandleDuplicateFiles = MagicMock()
        self.store = file_store.FileStore(self.mockHandleDuplicateFiles, self.mockHash)

    def test_can_add_file_to_file_store(self):
        self.store.Add("myFile")

        self.assertEqual(self.store.file_set, {HASH_RETURN_VALUE})

    def test_adding_different_file_adds_another_entry_to_the_dictionary(self):
        self.store.Add("myFile")
        self.mockHash.return_value.digest.return_value = DIFFERENT_HASH_RETURN_VALUE
        self.store.Add("myOtherFile")

        self.assertEqual(self.store.file_set, { HASH_RETURN_VALUE, DIFFERENT_HASH_RETURN_VALUE})

    def test_adding_two_files_with_different_name_same_content_only_adds_first_file(self):
        self.store.Add("myFile")
        self.store.Add("myFileWithSameContent")

        self.assertEqual(self.store.file_set, { HASH_RETURN_VALUE })

    def test_adding_a_duplicate_file_calls_the_duplicate_file_handling_function(self):
        self.store.Add("myFile")
        self.store.Add("myFileWithSameContent")

        self.mockHandleDuplicateFiles.assert_called_once_with("myFileWithSameContent")

if __name__ == '__main__':
    unittest.main()

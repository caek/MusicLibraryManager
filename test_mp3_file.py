import io
from mock import patch, MagicMock
import mp3_file

__author__ = 'chaynes'

import unittest

MP3_DATA = '12345' + '\x00' * 200

ID3_HEADER = 'ID3\x00\x00\x00\x00\x00\x00\x01\x00'
ID3_TRAILER = 'TAG' + '\x00' * (128 - len('TAG'))

class Mp3FileTest(unittest.TestCase):

    @patch('io.open', MagicMock(return_value=io.BytesIO(MP3_DATA)))
    def test_reading_file_with_no_header_returns_mp3_data(self):
        mp3 = mp3_file.Mp3File("myMp3File")

        self.assertEqual(MP3_DATA, mp3.data())

    @patch('io.open', MagicMock(return_value=io.BytesIO(ID3_HEADER+MP3_DATA)))
    def test_reading_file_with_header_returns_mp3_data(self):
        mp3 = mp3_file.Mp3File("myMp3File")

        self.assertEqual(MP3_DATA, mp3.data())

    @patch('io.open', MagicMock(return_value=io.BytesIO(MP3_DATA+ID3_TRAILER)))
    def test_reading_file_with_trailer_returns_mp3_data(self):
        mp3 = mp3_file.Mp3File("myMp3File")

        self.assertEqual(MP3_DATA, mp3.data())

    @patch('io.open', MagicMock(return_value=io.BytesIO(ID3_HEADER+MP3_DATA+ID3_TRAILER)))
    def test_reading_file_with_header_and_trailer_returns_mp3_data(self):
        mp3 = mp3_file.Mp3File("myMp3File")

        self.assertEqual(MP3_DATA, mp3.data())

if __name__ == '__main__':
    unittest.main()

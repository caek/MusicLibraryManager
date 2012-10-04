import io
import struct
from mutagen.id3 import BitPaddedInt

__author__ = 'chaynes'

def _id3_trailer_length(f):
    try:
        f.seek(-128, io.SEEK_END)
        idata = f.read(3)
        if idata == "TAG":
            return 128
    except IOError:
        pass
    return 0

def _id3_header_length(f):
    try:
        # technically an insize=0 tag is invalid, but we skip it anyway
        end = f.seek(0, io.SEEK_END)
        f.seek(0)
        idata = f.read(10)
        id3, insize = struct.unpack('>3sxxx4s', idata)
        insize = BitPaddedInt(insize)
        if id3 == 'ID3' and 0 <= insize <= end - 10:
            return insize + 10
    except (IOError, struct.error):
        pass
    return 0

class Mp3File(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def data(self):
        with io.open(self.file_name, "rb") as f:
            end = f.seek(0, io.SEEK_END)-_id3_trailer_length(f)
            start = _id3_header_length(f)
            f.seek(start)
            return f.read(end-start)
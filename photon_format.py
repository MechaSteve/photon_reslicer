from io import BufferedReader
import struct



class PhotonLayer:
    number : int = 0
    # build and manipulate RLE data as a mutable bytearray, store it as an immutable bytes object
    # provide method functions to uncompress and recompress image
    _dataRLE : bytes = bytes()

    lift_height : float = 6.0
    lift_speed : float = 2.0
    exposure : float = 3.0
    thickness : float = 0.05
    pixel_count : int = 0



class PhotonFile:
    name = 'unnamed'
    layers : list[PhotonLayer] = []


    def read_file(f : BufferedReader):
        photon_struct = struct.Struct('12s4B8l12sl10f3l2fl?3l')
        file_unpack = photon_struct.unpack(f.read(photon_struct.size))




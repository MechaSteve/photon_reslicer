from ast import Bytes
import struct
from typing import Union


class PhotonLayer:
    number : int = 0
    # build and manipulate RLE data as a mutable bytearray, store it as an immutable bytes object
    dataRLE : bytes = Bytes()

    lift_height : float = 6.0
    lift_speed : float = 2.0
    exposure : float = 3.0
    thickness : float = 0.05
    pixel_count : int = 0


class PhotonFile:
    name = 'unnamed'
    layers : list[PhotonLayer] = []




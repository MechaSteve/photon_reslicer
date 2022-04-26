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
        photon_struct = struct.Struct('12s4B8L12sl10f3l2fl?3l')
        file_unpack = photon_struct.unpack(f.read(photon_struct.size))
        # 0x00 [0] : ANYCUBIC
        vendor_name = file_unpack[0].decode()
        # 0x0C [1] : Version number primary (uint8)
        # 0x0D [2] : Version number major revision (uint8)
        # 0x0E [3] : Version number minor revision (uint8)
        # 0x0F [4] : Verison number update number (uint8)
        version_str = 'V{}.{%02d}.{%02d}.{%02d}'.format(file_unpack[1], file_unpack[2], file_unpack[3], file_unpack[4])
        # 0x10 [5] : Area number (meaning? int32) 
        # 0x14 [6] : File Header Addresss, always 0x30 (uint32)
        # 0x18 [7] : Unknown Header Info (uint32)
        # 0x1C [8] : Preview address (uint32)
        # 0x20 [9] : Preview end address (uint32)
        # 0x24 [10]: Layer Definition address (uint32)
        # 0x28 [11]: Layer Definition end address (uint32)
        # 0x2C [12]: Layer Image Start address (uint32)
        # 0x30 [13]: File Header "HEADER"
        # 0x3C [14]: Header Length (uint32)
        # 0x40 [15]: pixel size, microns (float32)
        # 0x44 [16]: Layer thickness, mm (float32)
        # 0x48 [17]: Normal exposure, seconds (float32)
        # 0x4C [18]: Off Time, seconds (float32)
        # 0x50 [19]: Bottom Exposure, seconds (float32)
        # 0x54 [20]: Bottom Layer Count, layers (float32)
        # 0x58 [21]: Z Lift, mm (float32)
        # 0x5C [22]: Z Lift Speed, mm (float32)
        # 0x60 [23]: Z Drop Speed, mm (float32)
        # 0x64 [24]: Print Volume, ml (float32)
        # 0x68 [25]: Anti-aliasing grade (int32)
        # 0x6C [26]: X Resolution (int32)
        # 0x70 [27]: Y Resolution (int32)
        # 0x74 [28]: Weight, g (float32)
        # 0x58 [29]: Price, dollars (float32)
        # 0x58 [30]: Resin Type (int32)
        # 0x58 [31]: Use Individual Layer Parameters (boolean)
        # 0x58 [32]: print time, seconds (int32) 
        #




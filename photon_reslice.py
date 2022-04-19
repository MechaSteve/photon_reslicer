from io import BufferedReader
import pandas as pd
import numpy as np
import struct

def get_int32( source : BufferedReader) -> int:
    return int.from_bytes(source.read(4), 'little')


def get_float( source : BufferedReader) -> float:
    buffer = memoryview(source.read(4)).cast('f')
    return buffer[0]


try:
    with open("example_data\example.dlp", "rb") as f:

        mybytearray = bytearray()

        photon_struct = struct.Struct('12s4B8l12sl10f3l2fl?3l')
        file_unpack = photon_struct.unpack(f.read(photon_struct.size))
        print(file_unpack)

        # file_title = f.read(12).decode()
        # version_list = []
        # for i in range(4):
        #     version_list.append(int.from_bytes(f.read(1), 'little'))
        # file_version = 'V {:02d}.{:02d}.{:02d}.{:02d}'.format(version_list[0],version_list[1],version_list[2],version_list[3])
        # area_number = get_int32(f)
        # file_header_addr = get_int32(f)
        # unknown_header_info = get_int32(f)
        # preview_addr = get_int32(f)
        # preview_end_addr = get_int32(f)
        # layer_def_addr = get_int32(f)
        # layer_def_end_addr = get_int32(f)
        # layer_image_addr = get_int32(f)
        # file_header_title = f.read(12).decode()
        # file_header_size = get_int32(f)
        # pixel_size = get_float(f)
        # layer_thickness = get_float(f)


        # print(file_title)
        # print(file_version)
        # print('Header Address: {:x}'.format(file_header_addr))
        # print(file_header_title)
        # print('pixel size: {} \u00B5m'.format(pixel_size))
        # print('layer thickness: {:0.03f} mm'.format(layer_thickness))

except IOError:
    print('Error While Opening the file!')   
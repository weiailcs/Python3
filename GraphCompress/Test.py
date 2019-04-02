# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import cv2
import matplotlib.pyplot as plt

import sys
import base64
import struct

# file_name = 'test.Compress'
#
# a = 255
# print(a, sys.getsizeof(a))
#
# b = chr(a)
# print(b, sys.getsizeof(b))
#
# a = [1, 2, 3]
#
# b = 1
# for i in a:
#     b = b << (len(bin(i)) - 2)
#     b = b | i
# print(bin(b), type(bin(b)), sys.getsizeof(b), b)
#
# with open(file_name, 'wb') as f:
#     f.write(b.to_bytes(len(bin(b)) - 2, byteorder='big'))
#
# c = bytes(0)
# with open(file_name, 'rb') as f:
#     c = f.read()
# print(int.from_bytes(bytes(c), byteorder='big'))
#
# print(16 >> 0 | 8)
#
# for i in range(10):
#     print(1 << i , end=' ')
#
# bit = [len(bin(x)) - 2 for x in range(256)]
# print(bit[255])


file_name = 'sample_3.bmp'
img = cv2.imread(file_name)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).flatten()
result = 1
for i in img:
    result = int(result << int(len(bin(i)) - 2)) | int(i)

with open('test.compress', 'wb') as f:
    f.write(result.to_bytes(len(bin(result)) - 2, byteorder='big'))

o = open('test_2.compress', 'wb')
for i in img:
    # print(int(i).to_bytes(8, byteorder='big'),end=' ')
    # print(len(int(i).to_bytes(len(bin(i)) - 2, byteorder='big')), end=' ')
    print(o.write(int(i).to_bytes(1, byteorder='big')), end=' ')
o.close()

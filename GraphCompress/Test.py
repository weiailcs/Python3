# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import cv2
import matplotlib.pyplot as plt

import sys
import base64
import struct

file_name = 'test.Compress'

a = 255
print(a, sys.getsizeof(a))

b = chr(a)
print(b, sys.getsizeof(b))

a = [1, 2, 3]

b = 1
for i in a:
    b = b << (len(bin(i)) - 2)
    b = b | i
print(bin(b), type(bin(b)), sys.getsizeof(b), b)

with open(file_name, 'wb') as f:
    f.write(bytes(b.to_bytes(len(bin(b)) - 2, byteorder='big')))

c = bytes(0)
with open(file_name, 'rb') as f:
    c = f.read()
print(int.from_bytes(bytes(c), byteorder='big'))

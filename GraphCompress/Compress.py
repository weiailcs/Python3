# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import cv2


class Compress:
    def __init__(self, file_name):
        try:
            self.img = cv2.imread(file_name)
        except ValueError:
            pass
        self.read_bitmap(file_name)
        self.compress()

    def read_bitmap(self, file_name):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        file_name = file_name.split('.')[0] + ".bmp"
        cv2.imwrite(file_name, self.img)

    def write_bitmap(self):
        pass

    def compress(self):
        print(self.img)
        pass

    def uncompress(self):
        pass


if __name__ == '__main__':
    compress = Compress("sample_1.bmp")
    # a = cv2.imread("sample_1.bmp", cv2.IMREAD_GRAYSCALE)
    # b = cv2.imread("sample_1.bmp")
    # b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    # print(a == b)

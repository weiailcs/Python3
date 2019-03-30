# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import cv2


class Compress:
    def __init__(self, file_name):
        self.col = 0
        self.row = 0

        try:
            self.img = cv2.imread(file_name)
        except ValueError:
            pass
        self.read_bitmap(file_name)
        self.img = self.two_dimensional_to_one_dimensional(self.img)
        self.compress()

    def read_bitmap(self, file_name):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        file_name = file_name.split('.')[0] + ".bmp"
        cv2.imwrite(file_name, self.img)

    def write_bitmap(self):
        pass

    def compress(self):
        len = self.img.shape[0]
        dp = np.zeros(len)
        for i in range(len):
            for j in range(i+1,len):
                dp[i] = min(dp[j])
        pass

    def uncompress(self):
        pass

    def two_dimensional_to_one_dimensional(self, matrix):
        vector = np.zeros(0, dtype=np.int)
        self.row, self.col = np.shape(self.img)
        for i in range(self.row):
            vector = np.append(vector, matrix[i][::(-1) ** (i % 2)])
        return vector


if __name__ == '__main__':
    compress = Compress("sample_1.png")
    # a = cv2.imread("sample_1.bmp", cv2.IMREAD_GRAYSCALE)
    # b = cv2.imread("sample_1.bmp")
    # b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    # print(a == b)

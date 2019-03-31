# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import cv2
import wx


class Compress:

    # 压缩
    @classmethod
    def compress(cls, file_name):
        img_matrix = cls.read_bitmap(file_name)
        img_vector, img_row, img_col = cls.two_dimensional_to_one_dimensional(img_matrix)
        img_vector = cls.img_compress(img_vector)
        img_vector = np.append(np.array([img_row, img_col]), img_vector)
        cls.write_compress(file_name, img_vector)

    @classmethod
    def img_compress(cls, vector):
        return vector

    # 读取任意格式图像并转为灰度图，并且储存为bmp格式
    @classmethod
    def read_bitmap(cls, file_name):
        try:
            matrix = cv2.imread(file_name)
        except ValueError:
            wx.MessageBox(file_name + ' Not Found !')

        matrix = cv2.cvtColor(matrix, cv2.COLOR_BGR2GRAY)
        file_name = file_name.split('.')[0] + ".bmp"
        cv2.imwrite(file_name, matrix)
        return matrix

    # 二进制写压缩文件
    @classmethod
    def write_compress(cls, file_name, vector):
        file_name = file_name.split('.')[0] + ".compress"
        vector.tofile(file_name)

    # 二维转一维
    @classmethod
    def two_dimensional_to_one_dimensional(cls, matrix):
        row, col = matrix.shape
        vector = np.zeros(0, dtype=np.int)
        for i in range(row):
            vector = np.append(vector, matrix[i][::(-1) ** (i % 2)])
        print(row, col)
        return vector, row, col

    ########################################################################################

    ########################################################################################

    # 解压方法
    @classmethod
    def uncompress(cls, file_name):
        img_vector, img_row, img_col = cls.read_compress(file_name)
        img_matrix = cls.one_dimensional_to_two_dimensional(img_vector, img_row, img_col)
        cls.write_bitmap(file_name, img_matrix)
        pass

    # 二进制读取压缩文件
    @classmethod
    def read_compress(cls, file_name):
        vector = np.fromfile(file_name, dtype=np.int)
        return vector[2:], vector[0], vector[1]

    # 写入bmp格式的解压图片
    @classmethod
    def write_bitmap(cls, file_name, matrix):
        file_name = file_name.split('.')[0] + "_UnCompress.bmp"
        cv2.imwrite(file_name, matrix)
        pass

    # 一维转二维
    @classmethod
    def one_dimensional_to_two_dimensional(cls, vector, row, col):
        matrix = vector.reshape(row, col)
        for i in range(row):
            if i % 2 == 1:
                matrix[i] = matrix[i][::-1]
        return matrix


if __name__ == '__main__':
    Compress.compress("sample_1.png")
    Compress.uncompress("sample_1.compress")

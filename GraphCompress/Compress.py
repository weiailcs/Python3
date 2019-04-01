# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import cv2
import wx
import queue


class RMQ:
    def __init__(self, vector):
        self.max_point = np.zeros((len(vector) + 5, 20))
        for i in range(len(vector)):
            self.max_point[i + 1][0] = vector[i]

        j = 1
        while (1 << j) <= len(vector):
            i = 1
            while i + (1 << j) - 1 <= len(vector):
                p = (1 << (j - 1))
                self.max_point[i][j] = max(self.max_point[i][j - 1], self.max_point[i + p][j - 1])
                i = i + 1
            j = j + 1

    # O(1)询问
    def query(self, l, r):
        l = l + 1
        r = r + 1
        k = int(np.log2(r - l + 1))
        return int(max(self.max_point[l][k], self.max_point[r - (1 << k) + 1][k]))


class Compress:

    # 压缩
    @classmethod
    def compress(cls, file_name):
        img_matrix = cls.read_bitmap(file_name)
        img_vector, img_row, img_col = cls.two_dimensional_to_one_dimensional(img_matrix)
        img_segment = cls.divide_segment(img_vector)
        # img_vector = np.append(np.array([img_row, img_col]), img_vector)
        # cls.write_compress(file_name, img_vector)

    @classmethod
    def divide_segment(cls, vector):
        # TODO:
        vector = list(vector)
        vector = [0, 0, 0, 0, 255, 255, 0, 0]

        # 初始化
        bit = [len(bin(x)) for x in range(256)]
        vector_bit = [bit[x] for x in vector]
        q = RMQ(vector_bit)
        block_size = 256
        length = len(vector)
        dp = [0] * (length + 5)

        # (第i个位置后分段, 该段二进制为j个长度, 该段有k个数字)
        cut = [(0, 0, 0)] * (length + 5)

        print(length)

        # 分段
        for i in range(length):
            if i < block_size:
                dp[i] = q.query(0, i) * (i + 1) + 11
                cut[i] = (-1, q.query(0, i), i + 1)
            else:
                dp[i] = dp[i - block_size] + q.query(i - block_size + 1, i) * block_size + 11
                cut[i] = (-1, q.query(i - block_size + 1, i), block_size)

            for j in range(max(0, i - block_size + 1), i):
                tmp = dp[j] + q.query(j + 1, i) * (i - j) + 11
                if dp[i] > tmp:
                    dp[i] = tmp
                    cut[i] = (j, q.query(j + 1, i), (i - j))

        # 查询划分
        stack = []
        i = length - 1
        while i != -1:
            i = cut[i][0]
            stack.append(cut[i])
        stack.reverse()

        print(stack)

        return stack

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
        return vector, row, col

    ########################################################################################

    ########################################################################################


class UnCompress:
    # 解压方法
    @classmethod
    def uncompress(cls, file_name):
        img_vector, img_row, img_col = cls.read_compress(file_name)
        img_matrix = cls.one_dimensional_to_two_dimensional(img_vector, img_row, img_col)
        cls.write_bitmap(file_name, img_matrix)
        pass

    @classmethod
    def img_uncompress(cls, vector):
        # TODO
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
    Compress.compress("sample_3.png")
    # UnCompress.uncompress("sample_3.compress")

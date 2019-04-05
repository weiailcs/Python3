# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import cv2
import wx
import queue
import md5

import threading as tr
import _thread
import time

schedule = 0.0


class GuageFrame(wx.Frame):
    def __init__(self, path):
        wx.Frame.__init__(self, None, -1, 'Gauge Example', size=(500, 200))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("white")
        self.count = 0
        self.gauge = wx.Gauge(panel, -1, 100, (50, 50), (300, 20))
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        # 进度条自身绑定循环任务，监听进度
        self.gauge.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Center(True)
        # self.Show()

        t = tr.Thread(target=Compress.compress, args=(path,))
        # self.t.setDaemon(True)
        t.start()

    def OnIdle(self, event):
        time.sleep(0.2)
        self.count = schedule
        self.gauge.SetValue(self.count)
        if self.count == 100:
            # 到达计划进度，取消进度条
            # self.t.join()
            time.sleep(5)
            self.Destroy()

    def timer(self, no):
        time.sleep(0.1)
        self.count = self.count + 1


class RMQ:
    def __init__(self, vector):
        self.max_point = np.zeros((len(vector) + 5, 50))
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
        img_compress_result = cls.divide_segment(img_vector, img_row, img_col)
        cls.write_compress(file_name, img_compress_result)

    @classmethod
    def divide_segment(cls, vector, row, col):

        global schedule

        print('开始分段')

        vector = list(vector)

        # 初始化
        bit = [len(bin(x)) - 2 for x in range(256)]
        vector_bit = [bit[x] for x in vector]
        q = RMQ(vector_bit)
        block_size = 256
        length = len(vector)
        dp = [0] * (length + 5)

        # (第i个位置后分段, 该段二进制为j个长度, 该段有k个数字)
        cut = [(0, 0, 0)] * (length + 5)

        # 划分
        for i in range(length):
            schedule = i / length * 80

            if int(schedule) == schedule:
                print(schedule)

            if i < block_size:
                dp[i] = q.query(0, i) * (i + 1) + 11
                cut[i] = (-1, q.query(0, i), i + 1)
            else:
                dp[i] = dp[i - block_size] + q.query(i - block_size + 1, i) * block_size + 11
                cut[i] = (i - block_size, q.query(i - block_size + 1, i), block_size)

            for j in range(max(0, i - block_size + 1), i):
                tmp = dp[j] + q.query(j + 1, i) * (i - j) + 11
                if dp[i] > tmp:
                    dp[i] = tmp
                    cut[i] = (j, q.query(j + 1, i), (i - j))

        # 查询划分
        stack = []
        i = length - 1
        while i != -1:
            stack.append(cut[i])
            i = cut[i][0]
        stack.reverse()
        stack.append((-2, -2, -2))

        print('制作压缩')
        # 制作压缩int
        result = 1
        result = int((result << 32) | row)
        result = int((result << 32) | col)
        cnt = 0
        var_len = 0
        for i in range(len(vector)):
            schedule = i / len(vector) * 20 + 80

            if int(schedule) == schedule:
                print(schedule)

            if i == stack[cnt][0] + 1:
                var_len = stack[cnt][1]
                result = (result << 3) | int(stack[cnt][1] - 1)
                result = (result << 8) | int(stack[cnt][2] - 1)
                cnt = cnt + 1
            result = ((result << var_len) | int(vector[i]))

        return int(result)

    # 读取任意格式图像并转为灰度图，并且储存为bmp格式
    @classmethod
    def read_bitmap(cls, file_name):
        matrix = cv2.imread(file_name)

        matrix = cv2.cvtColor(matrix, cv2.COLOR_BGR2GRAY)
        file_name = file_name.split('.')[0] + ".bmp"
        cv2.imwrite(file_name, matrix)

        # matrix = np.array([[0, 0, 0], [255, 0, 0], [255, 255, 0]])

        return matrix

    # 二进制写压缩文件
    @classmethod
    def write_compress(cls, file_name, result):
        global schedule

        file_name = file_name.split('.')[0] + ".compress"

        length = len(bin(result)) - 2
        cnt = 8
        o = open(file_name, 'wb')

        while cnt <= length:
            o.write((result >> (length - cnt) & 255).to_bytes(1, byteorder='big'))
            cnt = cnt + 8

        if length % 8 != 0:
            o.write(((result & (2 ** (length % 8) - 1)) << (8 - length % 8)).to_bytes(1, byteorder='big'))
            o.write(int((8 - length % 8) % 8).to_bytes(1, byteorder='big'))
        else:
            o.write(int(0).to_bytes(1, byteorder='big'))
        o.close()

        schedule = 100

    # 二维转一维
    @classmethod
    def two_dimensional_to_one_dimensional(cls, matrix):
        row, col = matrix.shape
        vector = np.zeros(0, dtype=np.int)
        for i in range(row):
            vector = np.append(vector, matrix[i][::(-1) ** (i % 2)])
        return vector, row, col


######################################################################################################

######################################################################################################

class UnCompress:
    # 解压方法
    @classmethod
    def uncompress(cls, file_name):
        img_compress_result = cls.read_compress(file_name)
        img_uncompress_result, img_row, img_col = cls.merge_segment(img_compress_result)
        img_uncompress_result = np.array(img_uncompress_result)
        img_matrix = cls.one_dimensional_to_two_dimensional(img_uncompress_result, img_row, img_col)
        cls.write_bitmap(file_name, img_matrix)
        pass

    @classmethod
    def merge_segment(cls, compress_result):

        print('开始解压')

        uncompress_result = []
        r = compress_result & 111
        compress_result = compress_result >> (8 + r)

        tmp_len = 32
        length = len(bin(compress_result)) - 2
        row = int((compress_result >> (length - 1 - tmp_len)) & (2 ** tmp_len - 1))
        col = int((compress_result >> (length - 1 - tmp_len - tmp_len)) & (2 ** tmp_len - 1))

        cnt = 1 + 2 * tmp_len

        while cnt < length:
            cnt = cnt + 3
            var_len = ((compress_result >> (length - cnt)) & 7) + 1
            cnt = cnt + 8
            var_number = ((compress_result >> length - cnt) & 255) + 1

            for i in range(var_number):
                cnt = cnt + var_len
                uncompress_result.append((compress_result >> (length - cnt)) & (2 ** var_len - 1))

        return uncompress_result, row, col

    # 二进制读取压缩文件
    @classmethod
    def read_compress(cls, file_name):
        with open(file_name, 'rb') as f:
            result = f.read()
        result = int.from_bytes(bytes(result), byteorder='big')
        return result

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
    file_name = "D:\\Documents\\codeFiles\\Python3\GraphCompress\\4"

    app = wx.App()
    frame = GuageFrame(file_name + '.jpg')
    frame.Show()
    # 创建线程，设定延迟加载时间及间隔执行时间
    # _thread.start_new_thread(frame.timer, (0.5,))
    app.MainLoop()

    UnCompress.uncompress(file_name + ".compress")
    print(md5.md5sum(file_name + '.bmp') == md5.md5sum(file_name + '_UnCompress.bmp'))
    # img1 = cv2.imread(file_name + '.bmp')
    # img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    # img2 = cv2.imread(file_name + '_UnCompress.bmp')
    # img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # print(img1 == img2)
    pass

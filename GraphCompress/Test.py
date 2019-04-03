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
#
#
# file_name = 'sample_3.bmp'
# img = cv2.imread(file_name)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).flatten()
# result = 1
# for i in img:
#     result = int(result << int(len(bin(i)) - 2)) | int(i)
#
# with open('test.compress', 'wb') as f:
#     f.write(result.to_bytes(len(bin(result)) - 2, byteorder='big'))
#
# print(bin(0))
# o = open('test_2.compress', 'wb')
# o.write(int(1).to_bytes(1, byteorder='big'))
# o.write(int(0).to_bytes(1, byteorder='big'))
# o.close()
#
# with open('test_2.compress', 'rb') as f:
#     result = f.read()
# print(bin(int.from_bytes(bytes(result), byteorder='big')))


import wx


class Frame(wx.Frame):
    """Frame class."""

    def __init__(self, parent=None, id=-1, title='Title',
                 pos=wx.DefaultPosition, size=(400, 200)):
        """Create a Frame instance."""
        wx.Frame.__init__(self, parent, id, title, pos, size)

        self.text_id = wx.NewId()
        self.text = wx.TextCtrl(self, self.text_id)
        self.text.Bind(wx.EVT_RIGHT_UP, self.OnRightClick, id=self.text_id)

        self.statusbar = self.CreateStatusBar(1, 0)

        wx.CallAfter(self.call, 1, 'abc', name="ccc", help="test")
        wx.CallLater(5000, self.call, 'call after 100ms', name="test")

    def OnRightClick(self, event):
        wx.MessageBox("message window", "message", wx.OK, self)

    def call(self, *args, **kwargs):
        message = repr(args) + repr(kwargs)
        self.SetStatusText(message, 0)


class App(wx.App):
    """Application class."""

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


def main():
    app = App()
    app.MainLoop()


if __name__ == '__main__':
    main()

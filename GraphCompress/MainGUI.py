# -*- coding: utf-8 -*-

import wx
import os

file_path = ' '


class DirDialog(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"文件夹选择对话框")
        b = wx.Button(self, -1, u"文件夹选择对话框")
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)

    def OnButton(self, event):
        global file_path
        dlg = wx.FileDialog(self, u"选择文件", style=wx.DD_NEW_DIR_BUTTON | wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            file_path = dlg.GetPath()
            # print(file_path)
        dlg.Destroy()
        self.Destroy()


def get_file_path():
    return file_path


if __name__ == '__main__':
    frame = wx.App()
    app = DirDialog()
    app.Show()
    frame.MainLoop()

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class LoginFrame
###########################################################################

class LoginFrame(wx.Frame):

    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(300, 200), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        log_in_size = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"登录"), wx.VERTICAL)

        log_in_size.SetMinSize(wx.Size(300, 150))
        g_sizer_1 = wx.GridSizer(0, 2, 0, 0)

        self.UserNameText = wx.StaticText(log_in_size.GetStaticBox(), wx.ID_ANY, u"账号", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.UserNameText.Wrap(-1)
        g_sizer_1.Add(self.UserNameText, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.UserName = wx.TextCtrl(log_in_size.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.UserName.SetMinSize(wx.Size(120, 24))

        g_sizer_1.Add(self.UserName, 0, wx.ALL, 5)

        self.PassWordText = wx.StaticText(log_in_size.GetStaticBox(), wx.ID_ANY, u"密码", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.PassWordText.Wrap(-1)
        g_sizer_1.Add(self.PassWordText, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.PassWord = wx.TextCtrl(log_in_size.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.PassWord.SetMinSize(wx.Size(120, 24))

        g_sizer_1.Add(self.PassWord, 0, wx.ALL, 5)

        log_in_size.Add(g_sizer_1, 1, wx.EXPAND, 5)

        self.Accept = wx.Button(log_in_size.GetStaticBox(), wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        log_in_size.Add(self.Accept, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(log_in_size)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Show()

        # Connect Events
        self.Accept.Bind(wx.EVT_BUTTON, self.submmit)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def submmit(self, event):
        user_name = self.UserName.GetValue()
        pass_word = self.PassWord.GetValue()

        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    log_in_frame = LoginFrame()
    app.MainLoop()

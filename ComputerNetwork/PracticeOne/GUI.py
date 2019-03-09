# -*- coding: utf-8 -*-

import wx
import wx.xrc
import socket as sk

host = ('', 21568)
server = ('202.114.196.97', 21568)
client_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
client_socket.bind(host)


###########################################################################
## Class LoginFrame
###########################################################################

class LoginFrame(wx.Frame):

    def __init__(self, parent=None):

        self.user_name = ''
        self.pass_word = ''
        self.status = False

        ############################################

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
        self.PassWord.SetValue('123456')

        g_sizer_1.Add(self.PassWord, 0, wx.ALL, 5)

        log_in_size.Add(g_sizer_1, 1, wx.EXPAND, 5)

        self.Accept = wx.Button(log_in_size.GetStaticBox(), wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        log_in_size.Add(self.Accept, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(log_in_size)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Accept.Bind(wx.EVT_BUTTON, self.submmit)

        self.Show()

    def __del__(self):
        pass

    def log_in_check(self):
        '''
        登录检查
        '''
        if self.user_name == '' or self.pass_word == '':
            wx.MessageBox('不可为空')
        elif '#' in self.user_name or '#' in self.pass_word:
            wx.MessageBox('不可含#')
        else:
            out_string = '02#' + self.user_name + '#' + self.pass_word + '#'
            client_socket.sendto(out_string.encode(), server)
            in_string = client_socket.recv(1024).decode()
            print(in_string)

            if in_string == '02:01':
                self.status = True
                wx.MessageBox('登录成功')
                self.Close()
            elif in_string == '02:02':
                wx.MessageBox('密码错误')
            elif in_string == '02:03':
                wx.MessageBox('用户不存在')
            elif in_string == '02:04':
                wx.MessageBox('用户已登录')

    # Virtual event handlers, overide them in your derived class
    def submmit(self, event):
        '''
        Log in
        '''
        print('登录')
        self.user_name = self.UserName.GetValue()
        self.pass_word = self.PassWord.GetValue()
        self.log_in_check()


###########################################################################
## Class FriendListFrame
###########################################################################

class FriendListFrame(wx.Frame):

    def __init__(self, parent=None):
        self.user_name = ''

        #####################################################################

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"联系人", pos=wx.DefaultPosition, size=wx.Size(240, 600),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.Size(240, 260))

        FriendListSizer = wx.BoxSizer(wx.VERTICAL)

        FriendListSizer.SetMinSize(wx.Size(160, 200))
        self.button_1 = wx.Button(self, wx.ID_ANY, u"陈浩（20171001091）", wx.DefaultPosition, wx.DefaultSize, 0)
        FriendListSizer.Add(self.button_1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.button_2 = wx.Button(self, wx.ID_ANY, u"陈浩（20171001091）", wx.DefaultPosition, wx.DefaultSize, 0)
        FriendListSizer.Add(self.button_2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.button_3 = wx.Button(self, wx.ID_ANY, u"陈浩（20171001091）", wx.DefaultPosition, wx.DefaultSize, 0)
        FriendListSizer.Add(self.button_3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        FriendListSizer.AddSpacer(40)

        self.button__modify = wx.Button(self, wx.ID_ANY, u"修改密码", wx.DefaultPosition, wx.DefaultSize, 0)
        FriendListSizer.Add(self.button__modify, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(FriendListSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button_1.Bind(wx.EVT_BUTTON, self.button_1_clicked)
        self.button_2.Bind(wx.EVT_BUTTON, self.button_2_clicked)
        self.button_3.Bind(wx.EVT_BUTTON, self.button_3_clicked)
        self.button__modify.Bind(wx.EVT_BUTTON, self.button_modify_clicked)

        self.Show()

    def __del__(self):
        print('联系人 Destroy')
        pass

    # Virtual event handlers, overide them in your derived class
    def button_1_clicked(self, event):
        print('button_1_clicked')
        self.user_name = self.button_1.LabelText
        self.chat_dialog = ChatFrame(title=self.user_name[-12:-1], label=self.user_name[:-13])
        # chat_dialog.Destroy()
        event.Skip()

    def button_2_clicked(self, event):
        print('button_2_clicked')
        self.user_name = self.button_1.LabelText
        self.chat_dialog = ChatFrame(title=self.user_name[-12:-1], label=self.user_name[:-13])
        # chat_dialog.Destroy()
        event.Skip()

    def button_3_clicked(self, event):
        print('button_3_clicked')
        self.user_name = self.button_1.LabelText
        self.chat_dialog = ChatFrame(title=self.user_name[-12:-1], label=self.user_name[:-13])
        # chat_dialog.Destroy()
        event.Skip()

    def button_modify_clicked(self, event):
        print('button_modify_clicked')
        event.Skip()


###########################################################################
## Class ChatFrame
###########################################################################

class ChatFrame(wx.Frame):

    def __init__(self, parent=None, title=wx.EmptyString, label='USER'):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                           size=wx.Size(400, 450), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        ChatSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, label), wx.VERTICAL)

        self.in_textCtrl = wx.TextCtrl(ChatSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(400, 300), 0)
        ChatSizer.Add(self.in_textCtrl, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        SendSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.out_textCtrl = wx.TextCtrl(ChatSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(200, 100), 5)
        SendSizer.Add(self.out_textCtrl, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.send_button = wx.Button(ChatSizer.GetStaticBox(), wx.ID_ANY, u"发送", wx.DefaultPosition, wx.DefaultSize, 0)
        SendSizer.Add(self.send_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        ChatSizer.Add(SendSizer, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(ChatSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.send_button.Bind(wx.EVT_BUTTON, self.send_button_clicked)

        self.Show()

    def __del__(self):
        print('窗口 Destroy')
        pass

    # Virtual event handlers, overide them in your derived class
    def send_button_clicked(self, event):
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    # b = ChatFrame(title='222')
    b = FriendListFrame()
    app.MainLoop()

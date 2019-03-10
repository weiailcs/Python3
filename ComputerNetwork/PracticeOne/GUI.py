# -*- coding: utf-8 -*-

import wx
import wx.xrc
import socket as sk
import time
import threading as tr
import random
import xlrd

host = ('', random.randint(30000, 50000))
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
        self.UserName.SetValue('20171003994')

        g_sizer_1.Add(self.UserName, 0, wx.ALL, 5)

        self.PassWordText = wx.StaticText(log_in_size.GetStaticBox(), wx.ID_ANY, u"密码", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.PassWordText.Wrap(-1)
        g_sizer_1.Add(self.PassWordText, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.PassWord = wx.TextCtrl(log_in_size.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, wx.TE_PASSWORD)
        self.PassWord.SetMinSize(wx.Size(120, 24))
        self.PassWord.SetValue('12345678')

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
        print('登录窗口 Destroy')
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
        event.Skip()


#
# ###########################################################################
# ## Class FriendListFrame
# ###########################################################################
#
# class FriendListFrame(wx.Frame):
#     def __init__(self, parent=None, user_name='', pass_word='123456'):
#         self.user_name = user_name
#         self.pass_word = pass_word
#         self.friend_name = ''
#         self.chat_frame = ChatFrame()
#         self.chat_frame.Close()
#         #####################################################################
#
#         wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"联系人", pos=wx.DefaultPosition, size=wx.Size(240, 600),
#                           style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
#
#         self.SetSizeHints(wx.DefaultSize, wx.Size(240, 260))
#
#         FriendListSizer = wx.BoxSizer(wx.VERTICAL)
#
#         FriendListSizer.SetMinSize(wx.Size(160, 200))
#         self.button_1 = wx.Button(self, wx.ID_ANY, u"陈   浩（20171001091）", wx.DefaultPosition, wx.DefaultSize, 0)
#         FriendListSizer.Add(self.button_1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
#
#         self.button_2 = wx.Button(self, wx.ID_ANY, u"王瑞凡（20171000642）", wx.DefaultPosition, wx.DefaultSize, 0)
#         FriendListSizer.Add(self.button_2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
#
#         self.button_3 = wx.Button(self, wx.ID_ANY, u"吴龙永（20171003994）", wx.DefaultPosition, wx.DefaultSize, 0)
#         FriendListSizer.Add(self.button_3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
#
#         FriendListSizer.AddSpacer(40)
#
#         self.button__modify = wx.Button(self, wx.ID_ANY, u"修改密码", wx.DefaultPosition, wx.DefaultSize, 0)
#         FriendListSizer.Add(self.button__modify, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
#
#         self.SetSizer(FriendListSizer)
#         self.Layout()
#
#         self.Centre(wx.BOTH)
#
#         # Connect Events
#         self.button_1.Bind(wx.EVT_BUTTON, self.button_1_clicked)
#         self.button_2.Bind(wx.EVT_BUTTON, self.button_2_clicked)
#         self.button_3.Bind(wx.EVT_BUTTON, self.button_3_clicked)
#         self.button__modify.Bind(wx.EVT_BUTTON, self.button_modify_clicked)
#
#         self.Show()
#
#     def __del__(self):
#         print('联系人列表 Destroy')
#         pass
#
#     # Virtual event handlers, overide them in your derived class
#     def button_1_clicked(self, event):
#         global status
#         print('button_1_clicked')
#         self.friend_name = self.button_1.LabelText
#
#         if self.chat_frame.t.is_alive():
#             status = False
#
#         self.chat_frame = ChatFrame(title=self.friend_name[-12:-1], label=self.friend_name[:-13])
#         event.Skip()
#
#     def button_2_clicked(self, event):
#         global status
#         print('button_2_clicked')
#         self.friend_name = self.button_2.LabelText
#
#         if self.chat_frame.t.is_alive():
#             status = False
#
#         ChatFrame(title=self.friend_name[-12:-1], label=self.friend_name[:-13])
#         event.Skip()
#
#     def button_3_clicked(self, event):
#         global status
#         print('button_3_clicked')
#         self.friend_name = self.button_3.LabelText
#
#         if self.chat_frame.t.is_alive():
#             status = False
#
#         ChatFrame(title=self.friend_name[-12:-1], label=self.friend_name[:-13])
#         event.Skip()
#
# def button_modify_clicked(self, event):
#     global status
#     print('button_modify_clicked')
#     print(self.user_name)
#
#     if self.chat_frame.t.is_alive():
#         status = False
#
#     ModifyFrame(user_name=self.user_name, pass_word=self.pass_word)
#     event.Skip()
#
#


###########################################################################
## Class ChatFrame
###########################################################################

class ChatFrame(wx.Frame):

    def __init__(self, parent=None, friend_number=wx.EmptyString, friend_name='OPPOSITEUSER'):

        self.status = True;
        self.friend_number = friend_number
        self.friend_name = friend_name
        self.in_message = ''
        self.out_massage = ''

        ##########################################################
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=friend_number, pos=wx.DefaultPosition,
                          size=wx.Size(400, 450), style=wx.CAPTION)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        ChatSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, friend_name), wx.VERTICAL)

        self.in_textCtrl = wx.TextCtrl(ChatSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.Size(400, 300), style=wx.TE_READONLY | wx.TE_MULTILINE)
        ChatSizer.Add(self.in_textCtrl, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        SendSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.out_textCtrl = wx.TextCtrl(ChatSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size(200, 100), 5 | wx.TE_MULTILINE)
        SendSizer.Add(self.out_textCtrl, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.send_button = wx.Button(ChatSizer.GetStaticBox(), wx.ID_ANY, u"发送", wx.DefaultPosition, wx.DefaultSize, 0)
        SendSizer.Add(self.send_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.quit_button = wx.Button(ChatSizer.GetStaticBox(), wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        SendSizer.Add(self.quit_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        ChatSizer.Add(SendSizer, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(ChatSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.send_button.Bind(wx.EVT_BUTTON, self.send_button_clicked)
        self.quit_button.Bind(wx.EVT_BUTTON, self.quit_button_clicked)

        self.Show()

        self.status = True
        self.t = tr.Thread(target=self.receive_message)
        self.t.setDaemon(True)
        self.t.start()

    def __del__(self):
        print('聊天窗口 Destroy')
        pass

    def send_message(self):
        if self.out_massage == '':
            wx.MessageBox('消息不能为空')
        elif '#' in self.out_massage:
            wx.MessageBox('消息不能含有#')
        else:
            out_string = '03#' + self.friend_number + '#' + self.out_massage + '#'
            client_socket.sendto(out_string.encode(), server)
            print(self.out_massage)
            self.in_textCtrl.AppendText('我：\n')
            self.in_textCtrl.AppendText(self.out_massage + '\n')
            self.out_textCtrl.Clear()
            in_string = client_socket.recv(1024).decode()
            print(in_string)

    def receive_message(self):
        while self.status:
            out_string = '04#' + self.friend_number + '#'
            client_socket.sendto(out_string.encode(), server)
            in_string = client_socket.recv(1024).decode()
            print(in_string)
            unread = int(in_string[3:])
            while unread > 0 and self.in_textCtrl:
                out_string = '05#' + self.friend_number + '#'
                client_socket.sendto(out_string.encode(), server)
                in_string = client_socket.recv(1024).decode()
                unread_text = in_string[35:]
                print(unread_text)
                self.in_textCtrl.AppendText(self.friend_name + '：\n')
                self.in_textCtrl.AppendText(unread_text + '\n')
                unread = unread - 1
            time.sleep(10)

    # Virtual event handlers, overide them in your derived class
    def send_button_clicked(self, event):
        print('消息发送')
        self.out_massage = self.out_textCtrl.GetValue()
        self.send_message()
        event.Skip()

    def quit_button_clicked(self, event):
        print('关闭')
        self.status = False
        self.Close()
        pass


###########################################################################
## Class MenuFrame
###########################################################################

class MenuFrame(wx.Frame):

    def __init__(self, parent=None, user_name='', pass_word=''):
        self.user_name = user_name
        self.pass_word = pass_word
        self.friend_name = ''
        self.friend_number = ''

        ##############################################################################
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(470, 297), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer3.SetMinSize(wx.Size(200, 160))
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer4.SetMinSize(wx.Size(200, 160))
        self.friend_name_ctrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.friend_name_ctrl, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.search_button = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.search_button, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer3.Add(bSizer4, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.button_modify = wx.Button(self, wx.ID_ANY, u"修改密码", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.button_modify, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.search_button.Bind(wx.EVT_BUTTON, self.search_button_clicked)
        self.button_modify.Bind(wx.EVT_BUTTON, self.button_modify_clicked)

        self.Show()

    def __del__(self):
        pass

    def find_number(self):
        data = xlrd.open_workbook('2017.xlsx')
        table = data.sheet_by_index(0)
        # print(str(table.col(0)[1])[6:-1])
        for i in range(table.nrows):
            if table.col(1)[i].value == self.friend_name:
                self.friend_number = str(table.col(0)[i])[6:-1]
                if str(self.friend_number) == str(self.user_name):
                    wx.MessageBox('不能联系自己')
                    return False
                return True
        wx.MessageBox('查无此人')
        return False

    # Virtual event handlers, overide them in your derived class
    def search_button_clicked(self, event):
        self.friend_name = self.friend_name_ctrl.GetValue()
        # self.find_number()
        if self.friend_name == '':
            wx.MessageBox('不能为空')
        else:
            if self.find_number():
                self.friend_name_ctrl.Clear()
                ChatFrame(friend_number=self.friend_number, friend_name=self.friend_name)
        event.Skip()

    def button_modify_clicked(self, event):
        print('button_modify_clicked')
        ModifyFrame(user_name=self.user_name, pass_word=self.pass_word)
        event.Skip()


###########################################################################
## Class ModifyFrame
###########################################################################

class ModifyFrame(wx.Frame):

    def __init__(self, parent=None, user_name='', pass_word=''):
        self.user_name = user_name
        self.pass_word = pass_word

        ############################################

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(300, 200), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        ModifySize = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"修改密码"), wx.VERTICAL)

        ModifySize.SetMinSize(wx.Size(300, 150))
        ModifySizer = wx.GridSizer(0, 2, 0, 0)

        self.PassWordText = wx.StaticText(ModifySize.GetStaticBox(), wx.ID_ANY, u"密码", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.PassWordText.Wrap(-1)
        ModifySizer.Add(self.PassWordText, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.PassWord = wx.TextCtrl(ModifySize.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, wx.TE_PASSWORD)
        self.PassWord.SetMinSize(wx.Size(120, 24))

        ModifySizer.Add(self.PassWord, 0, wx.ALL, 5)

        self.CheckPassWordText = wx.StaticText(ModifySize.GetStaticBox(), wx.ID_ANY, u"确认密码", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.CheckPassWordText.Wrap(-1)
        ModifySizer.Add(self.CheckPassWordText, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.CheckPassWord = wx.TextCtrl(ModifySize.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, wx.TE_PASSWORD)
        self.CheckPassWord.SetMinSize(wx.Size(120, 24))

        ModifySizer.Add(self.CheckPassWord, 0, wx.ALL, 5)

        ModifySize.Add(ModifySizer, 1, wx.EXPAND, 5)

        self.Accept = wx.Button(ModifySize.GetStaticBox(), wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        ModifySize.Add(self.Accept, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(ModifySize)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Accept.Bind(wx.EVT_BUTTON, self.submmit)

        self.Show()

    def __del__(self):
        print('修改密码窗口 Destroy')
        pass

    def modify_check(self):
        new_pass_word = self.PassWord.GetValue()
        check_new_pass_word = self.CheckPassWord.GetValue()

        if '#' in self.user_name or '#' in self.pass_word:
            wx.MessageBox('不可含#')
        else:
            out_string = '01#' + self.user_name + '#' + self.pass_word + '#' + new_pass_word + '#' + check_new_pass_word + '#'
            client_socket.sendto(out_string.encode(), server)
            in_string = client_socket.recv(1024).decode()
            print(in_string)

            if in_string == '01:01':
                wx.MessageBox('用户初始密码错误')
            elif in_string == '01:02':
                wx.MessageBox('两次密码不一致')
            if in_string == '01:03':
                wx.MessageBox('用户密码修改成功')
                self.Close()
            if in_string == '01:04':
                wx.MessageBox('用户不存在')

    # Virtual event handlers, overide them in your derived class
    def submmit(self, event):
        print('modify_button clicked')
        self.modify_check()
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    b = ChatFrame()
    app.MainLoop()

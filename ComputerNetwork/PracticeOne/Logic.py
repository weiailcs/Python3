# -*- coding: utf-8 -*-

'''
(1) 格式错误：00:00

(1) 用户初始密码错误：01:01
(2) 两次密码不一致：01:02
(3) 用户密码修改成功：01:03
(4) 用户不存在：01:04

(1) 登陆成功：02:01
(2) 密码错误：02:02
(3) 用户不存在：02:03
(4) 用户已登录：02:04

(1) 发送成功：03:01
(2) 对方离线：03:02

(1) 未接收消息条数: 04:条数

(1) 无未读消息：05:01

(1) 离线成功：06:01
(2) 已处于离线状态：06:02

(1) 未登录：07:01
'''

# 20171001091
# 123456

import wx
import socket as sk
from GUI import *

if __name__ == '__main__':
    app = wx.App()
    log_in = LoginFrame()
    app.MainLoop()
    if log_in.status:
        friend_list = FriendListFrame(user_name=log_in.user_name, pass_word=log_in.pass_word)
        app.MainLoop()

    # 注销
    client_socket.sendto('06#'.encode(), server)
    print(client_socket.recv(1024).decode())

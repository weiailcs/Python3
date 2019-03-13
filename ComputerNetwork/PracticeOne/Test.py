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

import wx
import socket as sk

host = ('', 21568)
server = ('202.114.196.97', 21568)
client_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
client_socket.bind(host)

a = '02#20171001091#123456#'
client_socket.sendto(a.encode(), server)
b = client_socket.recv(1024).decode()
print(b)

a = '06#'
client_socket.sendto(a.encode(), server)
b = client_socket.recv(1024).decode()
print(b)

if __name__ == '__main__':
    pass

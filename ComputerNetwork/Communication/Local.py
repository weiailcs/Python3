# -*- coding:utf-8 -*-
import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = '127.0.0.1'  # 获取本地主机名
port = 8483  # 设置端口好
s.connect((host, port))

while True:
    print(s.recv(1024).decode())
s.close()

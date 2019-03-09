# -*- coding: utf-8 -*-

from socket import *

host = '202.114.196.97'
port = 80
addr = (host, port)
data = b'GET /net HTTP/1.1\r\nAccept-Encoding: identity\r\nHost:se.cug.edu.cn\r\nConnection: close\r\nUser - Agent: Python -urllib / 3.7\r\n\r\n'
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(addr)
tcpCliSock.send(data)
data_new = tcpCliSock.recv(1024).decode()

open_file = open('data_download.txt', 'w')
for var in data_new:
    open_file.writelines(var)
    open_file.write('\n')
open_file.close()

tcpCliSock.close()

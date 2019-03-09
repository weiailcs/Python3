# -*- coding: utf-8 -*-

import base64
from PIL import Image

from socket import *

HOST = '202.114.196.97'
PORT = 80
ADDR = (HOST, PORT)
data = b'GET /net/pmh.jpg HTTP/1.1\r\nAccept-Encoding: identity\r\nHost:se.cug.edu.cn\r\nConnection: close\r\nUser - Agent: Python -urllib / 2.7\r\n\r\n'
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
tcpCliSock.send(data)

data_new = tcpCliSock.recv(1024)
print(data_new)
data_new = data_new.decode()

open_file = open('picture_download.txt', 'w')
for var in data_new:
    open_file.writelines(str(var))
    open_file.write('\n')
open_file.close()

tcpCliSock.close()

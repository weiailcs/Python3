# -*- coding: utf-8 -*-

import socket as sk
import threading as tr

outString = ""
inString = ""
nick_name = ""


def send_data(sock):
    '''消息发送方法'''
    global nick_name, outString
    while True:
        outString = input()
        sock.send(outString.encode())


def receive_data(sock):
    '''接收消息方法'''
    global inString
    while True:
        inString = sock.recv(1024)
        print('Server : ' + inString.decode())


nick_name = input("input your nick name: ")
# server_ip_address = input("input server ip address: ")
server_ip_address = '66.42.71.214'
port_number = 5214

sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)  # 创建套接字，默认为ipv4
sock.connect((server_ip_address, port_number))  # 发起连接服务请求，发出的是一个元组

sock.send(nick_name.encode())  # 登陆

receive_thread = tr.Thread(target=receive_data, args=(sock,))  # 接收消息线程
receive_thread.start()

send_thread = tr.Thread(target=send_data, args=(sock,))  # 发送消息线程
send_thread.start()

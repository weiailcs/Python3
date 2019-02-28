# -*-coding:utf-8-*-

import socket as sk
import threading as tr

con = tr.Condition
server_ip_address = '192.168.146.128'
port_number = 8484
data = ''


def receive_data(connection, nick_name):
    global data
    while True:
        data = connection.recv(1024)
        print(nick_name + ' : ' + data.decode())


def send_data(connection, nick_name):
    global data
    while True:
        tmp = input()
        connection.send(tmp.encode())


sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
print('套接字建立\n')
sock.bind((server_ip_address, port_number))
sock.listen(5)

connection, client_ip_address_and_port_number = sock.accept()
print('连接建立\n')
nick_name = connection.recv(1024)
nick_name = nick_name.decode()
tr.Thread(target=receive_data, args=(connection, nick_name)).start()
tr.Thread(target=send_data, args=(connection, nick_name)).start()

# -*- coding: utf-8 -*-

from tkinter import *
from socket import *
import random

ADDR = ("202.114.196.97", 21568)
host = ('', random.randint(30000, 50000))
udpCliSock = socket(AF_INET, SOCK_DGRAM)
udpCliSock.bind(host)

root = Tk()

root.title(('copyQQ'.encode("utf-8").decode("utf-8")))
root.geometry('400x150')

label1 = Label(root, text='账号：')
label1.place(x=50, y=20)

label2 = Label(root, text='密码：')
label2.place(x=50, y=80)

e1 = StringVar()
e2 = StringVar()
e1.set('20171003994')

eny1 = Entry(root, textvariable=e1, width=25)
eny2 = Entry(root, textvariable=e2, width=25)
eny1.place(x=100, y=20)
eny2.place(x=100, y=80)


def denglu(e1, e2):
    data = '02#' + e1.get() + '#' + e2.get() + '#'
    tongxin(data)


def zuce(a1, a2, a3):
    data = '01#' + a1.get() + '#' + a2.get() + '#' + a3.get() + '#'
    tongxin(data)


def gaimi(a1, a2, a3, a4):
    data = '01#' + a1.get() + '#' + a2.get() + '#' + a3.get() + '#' + a4.get() + '#'
    tongxin(data)


def tongxin(data):  # 登录
    print(data)
    udpCliSock.sendto(data.encode('utf-8'), ADDR)
    data1, addr = udpCliSock.recvfrom(1024)
    # udpCliSock.close()
    str1 = Reply1(data1.decode())
    create_window(str1)


def create_window(str):
    quit_window = Toplevel()
    root.title(('copyQQ'.encode("utf-8").decode("utf-8")))
    root.geometry('400x150')
    quit_label = Label(quit_window, text=str)
    quit_label.pack()


def create_zhuche_window():
    zhuche_window = Toplevel()
    zhuche_window.title(('注册'.encode("utf-8").decode("utf-8")))
    zhuche_window.geometry('400x200')

    label1 = Label(zhuche_window, text='账号：')
    label1.place(x=50, y=20)
    label2 = Label(zhuche_window, text='密码：')
    label2.place(x=50, y=80)
    label3 = Label(zhuche_window, text='确认密码：')
    label3.place(x=50, y=140)

    a1 = StringVar()
    a2 = StringVar()
    a3 = StringVar()
    eny1 = Entry(zhuche_window, textvariable=a1, width=25)
    eny2 = Entry(zhuche_window, textvariable=a2, width=25)
    eny3 = Entry(zhuche_window, textvariable=a3, width=25)
    eny1.place(x=100, y=20)
    eny2.place(x=100, y=80)
    eny3.place(x=110, y=140)
    a1.set('20171000724')
    a2.set('123456')
    a3.set('123456')

    zhuceButton = Button(zhuche_window, text="注册", command=lambda: zuce(a1, a2, a3), activebackground='red')
    zhuceButton.place(x=320, y=80)


def create_gaimima_window():
    gaimima_window = Toplevel()
    gaimima_window.title(('修改密码'.encode("utf-8").decode("utf-8")))
    gaimima_window.geometry('400x250')

    label1 = Label(gaimima_window, text='账号：')
    label1.place(x=50, y=20)
    label2 = Label(gaimima_window, text='初始密码：')
    label2.place(x=50, y=80)
    label3 = Label(gaimima_window, text='新密码：')
    label3.place(x=50, y=140)
    label4 = Label(gaimima_window, text='确认新密码：')
    label4.place(x=50, y=200)

    a1 = StringVar()
    a2 = StringVar()
    a3 = StringVar()
    a4 = StringVar()
    eny1 = Entry(gaimima_window, textvariable=a1, width=25)
    eny2 = Entry(gaimima_window, textvariable=a2, width=25)
    eny3 = Entry(gaimima_window, textvariable=a3, width=25)
    eny4 = Entry(gaimima_window, textvariable=a4, width=25)
    eny1.place(x=100, y=20)
    eny2.place(x=110, y=80)
    eny3.place(x=110, y=140)
    eny4.place(x=120, y=200)
    a1.set('20171000724')
    a2.set('123456')
    a3.set('123789')
    a4.set('123789')

    gaimima_Button = Button(gaimima_window, text="修改密码", command=lambda: gaimi(a1, a2, a3, a4), activebackground='red')
    gaimima_Button.place(x=320, y=80)


dengluButton = Button(root, text="登录", command=lambda: denglu(e1, e2), activebackground='red')
dengluButton.place(x=190, y=110)

zhucheButton = Button(root, text="注册", command=create_zhuche_window, activebackground='blue', relief="flat")
zhucheButton.place(x=300, y=18)

gaimimaButton = Button(root, text="忘记密码？", command=create_gaimima_window, activebackground='blue', relief="flat")
gaimimaButton.place(x=300, y=80)


def Reply1(str):
    print(str)
    # 01修改密码 01#账号#初始密码#新密码#确认密码#
    if str == '01:01':
        return '用户初始密码错误,请重新输入!'
    elif str == '01:02':
        return '两次密码不一致,请重新输入!'
    elif str == '01:03':
        return '用户修改密码成功'
    elif str == '01:04':
        return '用户不存在,请重新输入!'

    # 02用户登录   02#账号#密码#
    elif str == '02:01':
        return '登陆成功'
    elif str == '02:02':
        return '密码错误,请重新输入!'
    elif str == '02:03':
        return '用户不存在,请重新输入!'
    elif str == '02:04':
        return '用户已登录'

    # 07报错
    elif str == '07:01':
        return '没有登录!'


    # 00格式错误
    elif str == '00:00':
        return '错误消息,请重新输入'


def Reply2(str):
    print(str)
    # 01注册 01#账号#密码#确认密码#
    if str == '01:01':
        return '注册成功!'
    elif str == '01:02':
        return '两次密码不一致,请重新输入!'
    elif str == '01:03':
        return '用户已存在'


root.mainloop()

if __name__ == '__main__':
    pass

from tkinter import *
from tkinter.messagebox import *
from threading import Timer
from PIL import Image, ImageTk
from socket import *
from _thread import *
import datetime
import time
import json
from button import *


class chatwindow():
    def __init__(self, i1):
        self.chat = Tk()
        self.chat.title(('与xxx聊天中'.encode("utf-8").decode("utf-8")))
        # 创建几个frame作为容器
        self.i = i1
        self.udpCliSock = socket(AF_INET, SOCK_DGRAM)
        self.frame_left_top = Frame(self.chat, width=380, height=270, bg='white')
        self.frame_left_center = Frame(self.chat, width=380, height=100, bg='white')
        self.frame_left_bottom = Frame(self.chat, width=380, height=20)
        self.frame_right = Frame(self.chat, width=170, height=400, bg='white')
        ##创建需要的几个元素
        self.text_msglist = Text(self.frame_left_top)
        self.text_msg = Text(self.frame_left_center);
        self.button_sendmsg = Button(self.frame_left_bottom, text=('发送'.encode("utf-8").decode("utf-8")),
                                     command=self.sendmessage)
        # 创建一个绿色的tag
        self.text_msglist.tag_config('green', foreground='#008B00')
        # 使用grid设置各个容器位置
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_left_center.grid(row=1, column=0, padx=2, pady=5)
        self.frame_left_bottom.grid(row=2, column=0)
        self.frame_right.grid(row=0, column=1, rowspan=3, padx=4, pady=5)
        self.frame_left_top.grid_propagate(0)
        self.frame_left_center.grid_propagate(0)
        self.frame_left_bottom.grid_propagate(0)
        # 把元素填充进frame
        self.text_msglist.grid()
        self.text_msg.grid()
        self.button_sendmsg.grid(sticky=E)
        # 主事件循环
        self.chat.mainloop()

    # 发送按钮事件
    def sendmessage(self):
        # 在聊天内容上方加一行 显示发送人及发送时间
        msgcontent = ('我:'.encode("utf-8").decode("utf-8")) + time.strftime("%Y-%m-%d %H:%M:%S",
                                                                            time.localtime()) + '\n '
        self.text_msglist.insert(END, msgcontent, 'green')
        self.text_msglist.insert(END, self.text_msg.get('0.0', END))
        self.text_msg.delete('0.0', END)
        self.ADDR = ("localhost", 21569 + self.i)
        info = self.text_msg.get('1.0', END)
        info = info.encode('utf-8')
        self.udpCliSock.sendto(info, self.ADDR)
        data, self.ADDR = self.udpCliSock.recvfrom(1024)
        data = data.decode('utf-8')
        if data == "03:01":
            showinfo(title='提示', message='发送成功')
        elif data == '03:02':
            showinfo(title='提示', message="对象已离线")
        else:
            showinfo(title='123', message=data)
        """msgcontent2=('好友:'.encode("utf-8").decode("utf-8"))+time.strftime("%Y-%m-%d %H:%M:%S",
                                                                            time.localtime()) + '\n '
        self.text_msglist.insert(END, msgcontent, 'green')
        self.text_msglist.insert(END, data.decode('utf-8'))"""


def startbegin(t):
    start_new_thread(onewindow, (t,))


def onewindow(t):
    im = chatwindow(t)

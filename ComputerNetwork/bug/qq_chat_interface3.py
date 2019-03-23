from tkinter import *
import datetime
import time
import random
import socket as sk

host = ('', random.randint(30000, 50000))
server = ('202.114.196.97', 21568)
client_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
client_socket.bind(host)

root = Tk()
root.title(('与xxx聊天中'.encode("utf-8").decode("utf-8")))


# 发送按钮事件
def sendmessage():
    # 在聊天内容上方加一行 显示发送人及发送时间
    msgcontent = ('我:'.encode("utf-8").decode("utf-8")) + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n '
    text_msglist.insert(END, msgcontent, 'green')
    text_msglist.insert(END, text_msg.get('0.0', END))
    data = text_msg.get('0.0', END)

    client_socket.sendto(data.strip().encode(), server)
    data = client_socket.recv(1024)
    print(data.decode())

    text_msg.delete('0.0', END)


# 创建几个frame作为容器
frame_left_top = Frame(width=380, height=270, bg='white')
frame_left_center = Frame(width=380, height=100, bg='white')
frame_left_bottom = Frame(width=380, height=20)
frame_right = Frame(width=170, height=400, bg='white')
##创建需要的几个元素
text_msglist = Text(frame_left_top)
text_msg = Text(frame_left_center);
button_sendmsg = Button(frame_left_bottom, text=('发送'.encode("utf-8").decode("utf-8")), command=sendmessage)
# 创建一个绿色的tag
text_msglist.tag_config('green', foreground='#008B00')
# 使用grid设置各个容器位置
frame_left_top.grid(row=0, column=0, padx=2, pady=5)
frame_left_center.grid(row=1, column=0, padx=2, pady=5)
frame_left_bottom.grid(row=2, column=0)
frame_right.grid(row=0, column=1, rowspan=3, padx=4, pady=5)
frame_left_top.grid_propagate(0)
frame_left_center.grid_propagate(0)
frame_left_bottom.grid_propagate(0)
# 把元素填充进frame
text_msglist.grid()
text_msg.grid()
button_sendmsg.grid(sticky=E)
# 主事件循环
root.mainloop()
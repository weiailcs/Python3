from button import *


class login():
    def __init__(self):
        self.window = Tk()
        self.window.minsize(width=455, height=300)
        self.window.title("暴雪登录")
        image = Image.open('暴雪.png')
        img = ImageTk.PhotoImage(image)
        self.canvas1 = Canvas(self.window, width=image.width, height=image.height, bg='white')
        self.canvas1.create_image(0, 0, image=img, anchor="nw")
        self.canvas1.create_image(image.width, 0, image=img, anchor="nw")
        self.canvas1.pack()
        self.L1 = Label(self.window, text="QQ号")
        self.L1.pack()
        self.E1 = Entry(self.window, width=30, bd=0, relief=FLAT)
        self.E1.pack()
        self.L2 = Label(self.window, text="密码")
        self.L2.pack()
        self.E2 = Entry(self.window, width=30, bd=0, relief=FLAT)
        self.E2.pack()
        self.loginin = Button(width=5, height=1, text="登录", activebackground="red", relief=FLAT, command=self.log)
        self.signup = Button(width=5, height=1, text="注册", activebackground="red", relief=FLAT,
                             command=self.alter_window)
        self.loginout = Button(width=5, height=1, text="退出", activebackground='red', relief=FLAT, command=self.quit)
        self.loginin.pack()
        self.signup.pack(side=LEFT)
        self.loginout.pack(side=RIGHT)
        self.window.mainloop()

    def quit(self):
        data = "06#" + self.E1.get()
        self.udpCliSock.sendto(data.encode(), self.ADDR)
        info, addr = self.udpCliSock.recvfrom(1024);
        info = info.decode()
        if info == "06:01":
            showinfo(title="提示", message="离线成功")
        else:
            showinfo(title="提示", message="失败")

    def log(self):
        self.ADDR = ("202.114.196.97", 21568)
        try:
            self.udpCliSock = socket(AF_INET, SOCK_DGRAM)
            ID = self.E1.get()
            keyword = self.E2.get()
            self.data = "02#" + ID + "#" + keyword + "#"
            udpCliSock.sendto(self.data.encode(), self.ADDR)
            order, self.ADDR = udpCliSock.recvfrom(1024)
            order = order.decode()
            if order == "02:01":
                showinfo(title='提示', message='登陆成功')
                button = MyApp(self.window, self.ADDR)
            elif order == "02:02":
                showinfo(title='提示', message="密码错误")
            elif order == "02:03":
                showinfo(title='提示', message="用户不存在")
            elif order == "02:04":
                showinfo(title='提示', message="用户已登录")
                button = MyApp(self.window, self.ADDR)
        except ConnectionResetError:
            showinfo(title='提示', message='网络错误')

    def alter_window(self):
        self.alter = Toplevel(self.window)
        self.L3 = Label(self.alter, text="QQ号")
        self.L3.pack()
        self.E3 = Entry(self.alter, width=30, bd=0, relief=FLAT)
        self.E3.pack()
        self.L4 = Label(self.alter, text="旧密码")
        self.L4.pack()
        self.E4 = Entry(self.alter, width=30, bd=0, relief=FLAT)
        self.E4.pack()
        self.L5 = Label(self.alter, text="新密码")
        self.L5.pack()
        self.E5 = Entry(self.alter, width=30, bd=0, relief=FLAT)
        self.E5.pack()
        self.L6 = Label(self.alter, text="确认密码")
        self.L6.pack()
        self.E6 = Entry(self.alter, width=30, bd=0, relief=FLAT)
        self.E6.pack()
        self.alter_key = Button(self.alter, width=5, height=1, text="确认修改", activebackground='red', relief=FLAT,
                                command=self.alter)
        self.alter_key.pack()
        self.alter.mainloop()

    def alter(self):
        ID1 = self.E3.get()
        key_w = self.E4.get()
        new_key = self.E5.get()
        sure_key = self.E6.get()
        try:
            ID = self.E1.get()
            keyword = self.E2.get()
            data = "01#" + ID1 + "#" + key_w + "#" + new_key + "#" + sure_key + "#"
            self.udpCliSock.sendto(data.encode(), self.ADDR)
            order, self.ADDR = udpCliSock.recvfrom(1024)
            order = order.decode()
            if order == "01;01":
                showinfo(title='提示', message='用户初始密码错误')
            elif order == "01:02":
                showinfo(title='提示', message='两次密码不一致')
            elif order == "01:03":
                showinfo(title='提示', message='修改密码成功')
                self.alter.destroy()
            elif order == "01:04":
                showinfo(title='提示', message="用户不存在")
        except ConnectionResetError:
            showinfo(title='提示', message='网络错误')


login = login()

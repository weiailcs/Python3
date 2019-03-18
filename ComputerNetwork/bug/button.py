# Tkinter is the module we will use to create the GUI.
from chat import *

udpCliSock = socket(AF_INET, SOCK_DGRAM)
i = 0


def geti():
    return i


def seti(num):
    global i
    i = num


# Your app is a subclass of the Tkinter class Frame.
class MyApp(Frame):

    # Constructor for our app.  The master parameter represents the root object
    # that will hold out application.  It is basically a window, with our application
    # existing in a frame inside that window.
    def __init__(self, master, addr):
        # Call the constructor of the Frame superclass.  The pad options create padding
        # between the edge of the Frame and the Widgits inside.
        Frame.__init__(self, master, padx=10, pady=10)
        # Give our window a title by calling the .title() method on the master object.
        master.title("Sample Application")
        # Set a minimum size through the master object, just to make our UI a little
        # nicer to look at.
        master.minsize(width=250, height=100)
        # .pack() is a necessary method to get our app ready to be displayed.  Packing
        # objects puts them in a simple column.  For a more complex way to arrange your
        # widgets, see .grid():
        # http://effbot.org/tkinterbook/grid.htm
        self.pack()
        self.ADDR = addr
        self.friends = {}
        with open('frienddata.json') as file1:
            self.friends = json.load(file1)
        # Now let's make some buttons using the Tkinter class Button.  The "text" parameter
        # indicates the text to be displayed in the button and the "command" parameter
        # specifies a procedure to execute if the button is clicked.  In this app, we will
        # have buttons that increase and decrease a variable.
        self.upButton = Button(self, text="friend1", command=self.increment)
        self.upButton.grid()  # Individual objects also must be packed to appear.
        self.downButton = Button(self, text="friend2", command=self.decrement)
        self.downButton.grid()
        self.quitButton1 = Button(self, text="chat_with_friend", command=self.start_communicate)
        self.quitButton1.grid()
        """self.quitButton2 = Button(self, text="friend4", command=self.create_quit_window)
        self.quitButton2.grid()
        self.quitButton3 = Button(self, text="friend5", command=self.create_quit_window)
        self.quitButton3.grid()
        self.quitButton4 = Button(self, text="friend6", command=self.create_quit_window)
        self.quitButton4.grid()
        self.quitButton11 = Button(self, text="friend7", command=self.create_quit_window)
        self.quitButton11.grid()
        self.quitButton21 = Button(self, text="friend8", command=self.create_quit_window)
        self.quitButton21.grid()
        self.quitButton31 = Button(self, text="friend9", command=self.create_quit_window)
        self.quitButton31.grid()
        self.quitButton41 = Button(self, text="friendA", command=self.create_quit_window)
        self.quitButton41.grid()"""
        self.addfriend = Button(self, text="add friends", command=self.addfriends)
        self.addfriend.grid()

        # The variable that we'll be incrementing and decrementing.
        self.value = 0
        # When you want to integrate a variable with your Widgets (eg buttons, labels, etc),
        # you make it a special type of Tkinter variable.  In this case, a StringVar.  There
        # is also IntVar, DoubleVar, and BooleanVar.  These are essentially mutable versions
        # of primitive types.  If we assign a normal string varaible to be the text of a button,
        # then change that string variable, the text of the button would be unchanged.  If we
        # instead use a StringVar, the button text will update automatically.  You'll see!
        self.value_str = StringVar()
        self.value_str.set("0")  # You set all Tkinter variable objects with the .set() method.

        # A Label to display our value.  Labels are like buttons except with no click effect.
        # Note that we use the textvariable parameter instead of text so that the text on
        # this label will automatically update with our StringVar.
        self.valueLabel = Label(self, textvariable=self.value_str)
        self.valueLabel.grid()

        # Lastly, a quit button, which will call the .create_quit_window() method defined below,
        # which displays a new window asking whether the user want's to quit.
        self.quitButton = Button(self, text="Quit", command=self.create_quit_window)
        self.quitButton.grid()
        self.mainloop()

    # Methods that will be called when the up and down buttons are pressed.
    def increment(self):
        self.value += 1
        # When we reset the value of the StringVar, the text on valueLabel will change!
        self.value_str.set(str(self.value))

    def decrement(self):
        self.value -= 1
        self.value_str.set(str(self.value))

    # This method creates a new window (which will be a child of the master of our frame,
    # not of our frame itself).  The quit window will ask the user if they really want to quit.
    # If the user clicks yes, the application will close.  If they say no, the quit window
    # will close.
    def create_quit_window(self):
        # The Toplevel class makes a window.  It's simpler than the Frame class.  We will make
        # it a child of our application's master object, but since it is a Toplevel object, it
        # will create a whole new window rather than one that is part of the application window.
        quit_window = Toplevel(self.master)
        # Give our quit window a title and minimum size.
        quit_window.title("Quit?")
        quit_window.minsize(width=150, height=50)
        # Display a message to the user asking if they want to quit.
        quit_label = Label(quit_window, text="Are you sure you want to quit?")
        quit_label.pack()
        # We give our window a yes and no button.  One quits the application and one quits
        # the window.
        yes_button = Button(quit_window, text="Yes", command=self.quit)
        yes_button.pack()
        no_button = Button(quit_window, text="No", command=quit_window.destroy)
        no_button.pack()

    def start_communicate(self):
        self.frlist = Toplevel(self)
        self.frlist.title('选择好友开始聊天')
        self.L = Label(self.frlist, text="请输入好友名称")
        self.L.pack()
        self.choice = Entry(self.frlist, width=30, bd=0, relief=FLAT)
        self.choice.pack()
        self.communicate = Button(self.frlist, width=5, height=1, text="开始聊天", activebackground="red", relief=FLAT,
                                  command=self.start)
        self.communicate.pack()
        listA = Listbox(self.frlist)
        for name in self.friends.keys():
            listA.insert(0, name)
        listA.pack(side=RIGHT)

        self.frlist.mainloop()

    def start(self):
        try:
            self.str1 = self.choice.get()
            start_new_thread(create_chat, (self.str1, self.ADDR))
            startbegin(geti())
            seti(geti() + 1)
        except KeyError:
            showinfo(title='提示', message='好友列表中暂无此好友')
        else:
            self.frlist.destroy()

    def addfriends(self):
        self.add_friend = Toplevel(self)
        self.add_friend.title("添加好友")
        self.friend_name = Entry(self.add_friend, width=30, bd=0, relief=FLAT)
        self.friend_name.pack()
        self.friend_ID = Entry(self.add_friend, width=30, bd=0, relief=FLAT)
        self.friend_ID.pack()
        self.get = Button(self.add_friend, width=5, height=1, text="添加", activebackground="red", relief=FLAT,
                          command=self.GOT)
        self.get.pack()
        self.add_friend.mainloop()

    def GOT(self):
        self.friends[self.friend_name.get()] = self.friend_ID.get()
        with open('frienddata.json', 'w') as file:
            json.dump(self.friends, file)
        self.add_friend.destroy()


def create_chat(ID, ADDR):
    # sock.append(socket(AF_INET, SOCK_DGRAM))
    # sock.append(socket(AF_INET, SOCK_DGRAM))
    udpSerSock = socket(AF_INET, SOCK_DGRAM)
    addr = ('', 21569 + geti())
    udpSerSock.bind(addr)
    while True:
        # 从聊天窗口接收消息
        data, addr = udpSerSock.recvfrom(1024)
        # print(data.decode('utf-8'), ADDR)
        answer = "03#" + ID + "#" + data.decode('utf-8') + "#"
        answer = answer.encode('utf-8')
        # answer = answer.encode('utf-8')
        # 发送至服务器
        udpCliSock.sendto(answer, ADDR)
        # 接收反馈消息
        info, ADDR = udpCliSock.recvfrom(1024)

        # info2,address=udpCliSock.recvfrom(1024)
        udpSerSock.sendto(info, addr)
    udpSerSock.close()
    udpCliSock.close()

    def func(self, ID):
        udpCliSock = socket(AF_INET, SOCK_DGRAM)
        while True:
            data = "04#" + ID + "#"
            data1 = "05#" + ID + "#"
            udpCliSock.sendto(data.encode(), self.ADDR)
            order2, self.ADDR = udpCliSock.recvfrom(1024)
            order2 = order2.decode()
            order2 = order2.count(3, -1)
            numofmes = int(order2)
            if numofmes != 0:
                udpCliSock.sendto(data1.encode(), self.ADDR)
                order3, self.ADDR = udpCliSock.recvfrom(1024)
                self.udpSerSock.sendto(order3, self.addr)
            else:
                break

    def ask(self):
        t = Timer(30.0, func)
        t.start()


# We make a Tk object to serve as the root of our interface.  We're making
# something to use as an argument for the master parameter, to be the "parent"
# of our frame.  We can use it to do things like set the size.  Other than
# that, you don't have to worry too much about this step.
"""root = Tk()"""
# Initialize our app object and run the Frame method .mainloop() to begin!
# You should see a small window with up and down buttons, a label displaying
# a number, and a quit button when you run this program.
# app = MyApp(root)
# app.mainloop()

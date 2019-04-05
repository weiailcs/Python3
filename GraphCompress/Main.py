# -*- coding: utf-8 -*-

from MainGUI import DirDialog, get_file_path
from Compress import GuageFrame, UnCompress
import _thread
import wx
import md5

if __name__ == '__main__':
    frame = wx.App()
    app = DirDialog()
    app.Show()
    frame.MainLoop()

    path = get_file_path()
    if path.find('\\'):
        path = path.replace('\\', '/')
    elif path.find('\\\\'):
        path = path.replace('\\\\', '/')

    print(path)
    file_name = path.split('.')[0]
    print(file_name)

    if str(path.split('.')[-1]) in ['bmp', 'png', 'jpg']:
        # Compress.compress(path)
        print('START')
        app = wx.App()
        frame = GuageFrame(path)
        frame.Show()
        # 创建线程，设定延迟加载时间及间隔执行时间
        # _thread.start_new_thread(frame.timer, (0.5, 0.2))
        app.MainLoop()

        UnCompress.uncompress(file_name + ".compress")
        print(md5.md5sum(file_name + '.bmp') == md5.md5sum(file_name + '_UnCompress.bmp'))
    else:
        wx.MessageBox('格式错误')

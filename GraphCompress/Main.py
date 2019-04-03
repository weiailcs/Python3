# -*- coding: utf-8 -*-

from MainGUI import *
from Compress import *

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
        Compress.compress(path)
        UnCompress.uncompress(file_name + ".compress")
        print(md5.md5sum(file_name + '.bmp') == md5.md5sum(file_name + '_UnCompress.bmp'))
    else:
        wx.MessageBox('格式错误')

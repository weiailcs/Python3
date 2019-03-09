# -*- coding: utf-8 -*-

from urllib.request import *

url = 'http://se.cug.edu.cn/'
data_new = urlopen(url)
print(data_new)
open_file = open('URLLIB.txt', 'w')
for var in data_new:
    open_file.writelines(var.decode('utf-8'))
    open_file.write('\n')
open_file.close()

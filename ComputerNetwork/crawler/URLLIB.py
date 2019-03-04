# -*- coding: utf-8 -*-

from urllib.request import *

url = 'https://www.google.com'
data = urlopen(url)
open_file = open('data.txt', 'w')
for var in data:
    open_file.writelines(str(var))
    open_file.write('\n')
open_file.close()

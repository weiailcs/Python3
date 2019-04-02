# -*- coding: utf-8 -*-

import hashlib


def md5sum(filepath):
    f = open(filepath, 'rb')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    f.close()
    return str(hash).upper()


if __name__ == '__main__':
    print(md5sum('sample_3.png'))

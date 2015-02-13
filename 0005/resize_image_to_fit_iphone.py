#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      illuz <iilluzen[at]gmail.com>
# File:        resize_image_to_fit_iphone.py
# Create Date: 2015-02-13 10:12:32
# Usage:       resize_image_to_fit_iphone.py directory
# Descripton:  resize image in a folder to fit iphone

"""
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""


import sys, os, shutil
from PIL import Image

iphone5_res = (640, 1136)

def resize_image(dir):
    walk = os.walk(dir)
    for root, dirs, files in walk:
        for file in files:
            print 'Dealing with', root + '/' + file, ":"
            # read
            im = Image.open(root + '/' + file)
            print '---Reading finished, size:', im.size
            if iphone5_res[0] > im.size[0] and \
                iphone5_res[1] > im.size[1]:
                   print '---Image size smaller enough.'
                   continue

            p = file.rfind('.')
            new_file = file[:p] + '_new' + file[p:]
            # # backup to _bak
            # shutil.copyfile(root + '/' + file, root + '/' + new_file)
            # print 'Backup to', root + '/' + new_file, '...'

            # resize
            newx = min(iphone5_res[0], im.size[0])
            newy = min(iphone5_res[1], im.size[1])
            im.resize((newx, newy)).save(root + '/' + new_file)
            print '---Resize successful, new size:', (newx, newy)


def main():
    if len(sys.argv) != 2:
        print "Need exactly 1 parameter!"
    else:
        try:
            resize_image(sys.argv[1])
        except IOError:
            print "Open directory or image error!"
            pass

if __name__ == '__main__':
    main()


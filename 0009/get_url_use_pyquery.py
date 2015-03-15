#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      illuz <iilluzen[at]gmail.com>
# File:        get_url_use_pyquery.py
# Create Date: 2015-03-12 15:16:03
# Usage:       get_url_use_pyquery.py page
# Descripton:  get url.

"""
第 0009 题：一个HTML文件，找出里面的链接。
"""

import sys
from pyquery import PyQuery

def main():
    if len(sys.argv) != 2:
        print('Argument error!')
    else:
        try:
            page = PyQuery(sys.argv[1])
        except:
            print('Wrong url!')
            print('Url is: ' + sys.argv[1])
            pass
        for elem in page('a'):
            print page(elem).attr('href')

if __name__ == '__main__':
    main()


#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      illuz <iilluzen[at]gmail.com>
# File:        get_html_body.py
# Create Date: 2015-03-15 21:07:33
# Usage:       get_html_body.py url

import sys
from pyquery import PyQuery as pq

def get_html_body(url):
    page = pq(url)
    print page('body').html().encode('utf-8', 'ignore')

def main():
    # get_html_body('http://mooc.guokr.com/post/610231/')
    if len(sys.argv) != 2:
        print("Need exact 1 parameter.")
    else:
        try:
            get_html_body(sys.argv[1])
        except Exception, e:
            print('There was something wrong', e)
            pass

if __name__ == '__main__':
    main()
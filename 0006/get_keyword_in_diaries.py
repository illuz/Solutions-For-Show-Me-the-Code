#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      illuz <iilluzen[at]gmail.com>
# File:        get_keyword_in_diaries.py
# Create Date: 2015-02-13 09:42:43
# Usage:       get_keyword_in_diaries.py directory
# Descripton:  get most words in a text

"""
第 0006 题：
你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""

import sys
import os
import re
from collections import Counter


def most_words_in_txt(file):
    c = Counter()
    with open(file, 'r') as text:
        # print list(text)
        for line in text:
            line = re.sub(r'[,.?!()]', ' ', line).lower()
            words = line.split()
            c += Counter(words)
    return c.most_common()[0]

def get_keyword_in_diaries(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            print 'In file ' +  root + '/' + file + ':',
            print most_words_in_txt(root + '/' + file)

def main():
    if len(sys.argv) != 2:
        print "Need exactly 1 parameter!"
    else:
        try:
            get_keyword_in_diaries(sys.argv[1])
        except IOError:
            print "Open directory or file error!"
            pass

if __name__ == '__main__':
    main()


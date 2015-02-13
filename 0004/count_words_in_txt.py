#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      illuz <iilluzen[at]gmail.com>
# File:        count_words_in_txt.py
# Create Date: 2015-02-13 09:12:43
# Usage:       count_words_in_txt.py file.txt [, file2.txt [...]]
# Descripton:  Count the words in a txt

"""
第 0004 题：
任一个英文的纯文本文件，统计其中的单词出现的个数。
"""


import sys
import re
from collections import Counter


def count_words(file):
    c = Counter()
    with open(file, 'r') as text:
        # print list(text)
        for line in text:
            line = re.sub(r'[,.?!()]', ' ', line).lower()
            words = line.split()
            c += Counter(words)
    cnt = 0
    for word in c.most_common():
        print word
        cnt += word[1]
    print 'Different kinds of words:', len(c)
    print 'Total words:', cnt


def main():
    if len(sys.argv) <= 1:
        print "Need at least 1 parameter."
    else:
        for file in sys.argv[1:]:
            try:
                count_words(file)
            except IOError:
                print "Open file error!"
                pass

if __name__ == '__main__':
    main()


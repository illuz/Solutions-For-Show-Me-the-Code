#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      illuz <iilluzen[at]gmail.com>
# File:        codes_analysis.py
# Create Date: 2015-02-15 21:47:54
# Usage:       codes_analysis.py [path of code folder]
# Descripton:  Analysis the code in a folder, count the code, blank line and comment.

"""
第 0007 题：
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""

import sys, os


# Counting examples (C++) :
# 1. '// comment'                       -> 0 code line, 1 comment line
# 2. 'while (1); // unlimited loop'     -> 1 code line, 1 comment line
# 3. 'while (1); /* unlimited loop'     -> 1 code line, 1 comment line
# 4. 'This style is ugly.*/ while (1);' -> 1 code line, 1 comment line

# There are some bugs here:
# '/* comment */'


# define the language and comment style
postfix_to_style = {
    'language': 'style_name',
    '.c':   'c',
    '.cpp': 'c',
    '.h':   'c',
    '.java':'c',

    '.py':  'python',

    '.html':'html',
    '.htm': 'html',

    '.sh':  'bash',
    '.bash':'bash'
}
comment_styles = {
    'style_name': ('inline', 'left_block', 'right_block'),
    'python': (r'#', r'"""', r"'''"),
    'c': (r'//', r'/*', r'*/'),
    'html': ('', r'<!--', r'-->'),
    'bash': (r'#', '', '') 
}



def analysis_single_file(file):
    """ return (the numbers of code, blank line, comment)"""
    print file, ':',
    code, blank_line, comment = 0, 0, 0
    try:
        with open(file, 'r') as text:
            postfix = os.path.splitext(file)[1]
            if postfix not in postfix_to_style:
                print 'Not code file'
                return 0, 0, 0
            style = comment_styles[ postfix_to_style[postfix] ]

            # the flag of block
            block = False

            for line in text:
                line = line.strip()
                # print line

                if line == '':
                    blank_line += 1
                    continue

                if block:
                    comment += 1

                    # 'cm */'
                    if style[2] == line[-len(style[2]):]:
                        block = False
                    # 'cm */ code'
                    elif style[2] in line:
                        block = False
                        code += 1
                else:
                    # '// cm'
                    if style[0] == line[:len(style[0])]:
                        comment += 1
                    # '/* cm'
                    elif style[1] == line[:len(style[1])]:
                        block = True
                        comment += 1
                    else:
                        code += 1
                        find_inline = line.find(style[0])
                        find_block = line.find(style[1])
                        if find_inline != -1 and find_block == -1:
                            # 'code // cm'
                            comment += 1
                        elif find_inline == -1 and find_block != -1:
                            # 'code /* cm'
                            comment += 1
                            block = True
                        elif find_inline > find_block:
                            # 'code // cm /* cm'
                            comment += 1
                        elif find_inline > find_block:
                            # 'code /* cm // cm'
                            comment += 1
                            block = True

                # print code, blank_line, comment
    except IOError:
        print 'Cannot open file', file
    print code, blank_line, comment
    return code, blank_line, comment

def analysis_folder(folder):
    code, blank_line, comment = 0, 0, 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            _cd, _bl, _cm = analysis_single_file(root + '/' + file)
            code += _cd
            blank_line += _bl
            comment += _cm
    print 'Total:', code, 'codes,', blank_line, 'blank lines,', comment, 'comments'

def main():
    if len(sys.argv) != 2:
        print "Need exactly 1 parameter!"
    else:
        try:
            analysis_folder(sys.argv[1])
        except IOError:
            print "Open directory error!"
            pass

if __name__ == '__main__':
    main()


#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      illuz <iilluzen[at]gmail.com>
# File:        create_keys_table_in_redis.py
# Create Date: 2015-02-13 00:25:48
# Usage:       create_keys_table_in_redis.py 
# Descripton:  solve show-me-the-code 0003

"""
第 0003 题：
将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
"""

from uuid import uuid4
import redis

def generate_key(num):
    return [str(uuid4()) for i in range(num)]

def write_to_redis(key_list):
    re = redis.StrictRedis(host='localhost', port=6379, db=0)
    for i in key_list:
        re.sadd('rkeys', i)

def main():
    write_to_redis(generate_key(200))

if __name__ == '__main__':
    main()


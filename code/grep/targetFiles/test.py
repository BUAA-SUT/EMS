#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/13
# @Anthor   : phantomDai
"""
testing read target file
"""

def read_4():
    content = []
    with open('follow_test', 'r') as file:
    # with open('MR11_17', 'r') as file:
        for aline in file:
            content.append(aline)

    file.close()
    print(content)
read_4()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/10/29
# @Anthor   : phantomDai
"""
统计“ＮＡ”的个数
"""


def get_number():
    counter = 1
    index = []
    with open("TestFrames_grep_no_repeat_1.2", 'r') as file:
        for line in file:
            temp_line = line.strip();
            if 'NA' in temp_line and 'NB' not in temp_line and 'CB' not in temp_line and 'WW' not in temp_line \
                    and 'EW' not in temp_line and 'BW' not in temp_line and 'EN' not in temp_line and 'NE' not in temp_line \
                    and 'NN' not in temp_line and 'BL' not in temp_line and 'EL' not in temp_line and 'LL' not in temp_line:
              index.append(counter)
            counter = counter + 1
    file.close()

    str_index = [str(ele) + '\n' for ele in index]

    file = open('need2anlysis4MR5', 'w+')
    file.writelines(str_index)
    file.close()


get_number()
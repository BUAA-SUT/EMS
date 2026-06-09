#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/1
# @Anthor   : phantomDai
"""
工具类
"""

import os
import numpy as np
import random
import re
import linecache


class Utl(object):
    """
    工具类，提供一些通用功能的接口
    """

    # 记录选择分区的次数
    counter = 0

    def __init__(self):
         self.counter = 0

    def get_file_object(self, file_path):
        """
        读取文件时，获取要读取文件的对象
        :param file_path: 要读取文件的名字
        :return: 文件对象
        """
        file = open(file_path, 'r')
        return file


    def write_test_cases(self, file_path, testcases):
        """
        将测试用例写入指定的文件中
        :param file_path: 要写入的文件的地址
        :param testcases: 要写入的测试用例
        :return: null
        """
        file = open(file_path, 'w+')
        file.writelines(testcases)
        file.close()
        print("ok!")

    def get_normal_literals(self, line_str):
        """
        获取pattern中的非元字符
        :param line_str:
        :return:
        """

        # 删掉patterns中的反向引用的数字,例如：\3
        line_str = re.sub(r'\\[0-9]', '', line_str)

        frist_non_normal_literal = ['[:alnum:]', '[:alpha:]', '[:cntrl:]', '[:digit:]',
                                    '[:xdigit:]', '[:punct:]', '[:space:]', '[:upper:]', '[:lower:]', '[:print:]',
                                    '[:blank:]']

        for item in frist_non_normal_literal:
            if "^" + item in line_str:
                if '[^' + item + ']' in line_str:
                    line_str = line_str.replace('[^' + item + ']', '')
                else:
                    line_str = line_str.replace("^" + item, '')
            else:
                if '[' + item + ']' in line_str:
                    line_str = line_str.replace('[' + item + ']', '')
                else:
                    line_str = line_str.replace(item, '')

        second_non_normal_literal = ["\\w", '\\W', '\\d', '\\D', '\\s', '\\S', '\\<', '\\>', '\\b', '\\B']

        for ele in second_non_normal_literal:
            if '[^' + ele + ']' in line_str:
                line_str = line_str.replace('[^' + ele + ']', '')
            if '[' + ele + ']' in line_str:
                line_str = line_str.replace('[' + ele + ']', '')
            if ele in line_str:
                line_str = line_str.replace(ele, '')

        third_non_normal_literal = ['.', '*', '?', '+', '$', '|', '^']

        line_str_list = [ele for ele in line_str]
        #存放删除以上'.', '*', '?', '+', '$', '|', '^'字符，除非他们前面有'\\'
        new_line_str_list = []

        for i in range(0, len(line_str)):
            if line_str_list[i] not in third_non_normal_literal:
                new_line_str_list.append(line_str_list[i])
            if line_str_list[i] in third_non_normal_literal:
                if i - 1 < 0 and i - 2 < 0:
                    continue
                if line_str_list[i - 1] != '\\':
                    continue
                if line_str_list[i - 1] == '\\':
                    new_line_str_list.append(line_str_list[i])

        line_str = ''.join(ele for ele in new_line_str_list)

        for ele in third_non_normal_literal:
            if '\\' + ele not in line_str and ele in line_str:
                line_str = line_str.replace(ele, '')

        # 去掉圆括号
        if '(' in line_str:
            temp_list = [s for s in line_str]
            flag = False
            for i in range(0, len(temp_list)):
                if flag:
                    flag = False
                    continue
                if temp_list[i] == '(' or temp_list[i] == ')':
                    temp_list[i] = ''
                if temp_list[i] == '\\':
                    if i == len(temp_list) - 1:
                        continue
                    else:
                        if temp_list[i+1] == '(' or temp_list[i + 1] == ')':
                            flag = True
            line_str = ''.join(ele for ele in temp_list)

        # 去掉括号：[X-Y]和{.*}
        line_str = re.sub('\[\w-\w\]', '', line_str)
        line_str = re.sub('\{.*\}', '', line_str)
        if '\\(' not in line_str and '(' in line_str:
            line_str = line_str.replace('(', '')
        if '\\)' not in line_str and ')' in line_str:
            line_str = line_str.replace(')', '')

        # 处理[abc]这种情况：去掉[]
        normal_literals = re.match('\[.*\]', line_str)
        if normal_literals != None:
            line_str = line_str.replace('[', '').replace(']', '')
        if '[' in line_str and ']' in line_str:
            line_str = line_str.replace('[', '').replace(']', '')

        return line_str if line_str != '' else 'NULL'

    def write_info_from_dict(self,file_path, dict):

        file = open(file_path, 'w+')
        for key, value in dict.items():
            file.write('{key}:{value}'.format(key=key,value=value) + '\n')
        file.close()

    def get_concrete_test_case(self):
        """
        从testpool中获取测试用例,索引是行号
        :return:
        """
        file_path = os.path.join(os.path.abspath('.'), 'files', 'partition_scheme_testcases_1.2')
        testcases = ['Null']
        with open(file_path, 'r') as file:
            for aline in file:
                testcases.append(aline.strip())
        file.close()

        return testcases

    def get_line_content(self, filepath, line_index):
        """
        获取指定行的信息
        :param filepath: 要读取的文件的路径
        :param line_index: 要读取的文件的行数，从１开始
        :return: 该行的内容
        """
        return linecache.getline(filepath, line_index).strip()

    def random_select_MR(self, MR_list):
        """
        randomly select a MR from the MR list
        :param MR_list:
        :return: the name of selected MR
        """
        index = random.randint(0, len(MR_list) - 1)

        return MR_list[index]

    def generate_follow_test_case(self, MR_name, source_test_case, source_test_case_index):
        """
        根据选择的蜕变关系以及原始测试用例生成衍生测试用例
        :param MR_name: 　选择的蜕变关系的名称
        :param source_test_case: 原始测试用例
        :return: 衍生测试用例
        """
        factory = MR_factory()
        MR_obj = factory.choose_MR(MR_name)
        return MR_obj.generate_follow_test_case(source_test_case, source_test_case_index)


    def get_partition_information(self):
        """
        从partition_scheme_testcases_file中获取分区的信息,键是分区的索引，值是包含该分区测试用例的ｌｉｓｔ
        :return: 字典
        """
        file_pth = os.path.join(os.getcwd('..'), 'partition', 'partition_scheme_testcases_file')

        partition_dict = {}
        with open(file_pth, 'r') as file:
            tricktrock = 1
            for aline in file:
                temp_testcases = aline.strip().split('[')[1].replace(']', '').replace(')', '').split(', ')
                partition_dict[str(tricktrock)] = temp_testcases
                tricktrock += 1
        file.close()

        return partition_dict


    def get_test_case_2_MRs(self):
        """
        获取测试用力与蜕变关系的映射关系
        :return: 字典:键是测试用例的编号，值是该测试用例可以作用的蜕变关系
        """

        test_case_2_MRs = {}

        file_path = os.path.join(os.path.abspath('..'), 'mapping relation', 'testcase_2_MRs')

        with open(file_path, 'r') as file:
            for aline in file:
                line_index = aline.strip().split(':')[0]
                MRs = aline.strip().split(':')[1].replace('[', '').replace(']', '').split(', ')
                test_case_2_MRs[line_index] = MRs
        file.close()

        return test_case_2_MRs


    def get_test_frames(self):
        """
        从TestFrames_grep_no_repeat_1.2中获取测试帧的信息
        :return: 字典: 键是测试用例的编号，值是该测试用例对应的选项的组合
        """

        file_path = os.path.join(os.getcwd('..'), 'files', 'TestFrames_grep_no_repeat_1.2')
        test_frames = {}
        with open(file_path, 'r') as file:
            tricktrock = 1
            for aline in file:
                choices = aline.strip().split(';')
                test_frames[str(tricktrock)] = choices
                tricktrock += 1

        file.close()
        return test_frames


if __name__ == '__main__':
    tool = Utl()
    test_case_path = os.path.join(os.path.abspath('..'), 'mapping relation', 'input')
    parent_path = os.path.join(os.path.abspath('..'), 'mapping relation')
    pure_literals = []
    with open(test_case_path, 'r') as test_cases_file:
        for aline in test_cases_file:
            pure_literals.append(tool.get_normal_literals(aline.strip()) + '\n')
    test_cases_file.close()
    MR_path = os.path.join(parent_path, 'normal_literals')
    tool.write_test_cases(MR_path, pure_literals)

    # print(tool.get_normal_literals(r'[d-i](.)(\s)([[:upper:]])(\d)\?(\W)'))






























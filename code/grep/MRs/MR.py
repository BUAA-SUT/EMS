#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/5
# @Anthor   : phantomDai
"""
the abstract class
"""
import abc
import os
from random import shuffle
import random

from myutl.MR_Utl import MyUtl
from myutl.Utl import Utl
import linecache


class MR(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        raise Exception('You must reimplement this method!')

    @abc.abstractmethod
    def verify_results(self, output_source, output_follow):
        raise Exception('You must reimplement this method')


"""
the implemention of MR1
"""


class MR1(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR1
        :param source_test_case:
        :return: follow-up test case
        """
        # 获取范围集合
        range_character_set = self.mr_utl.get_range_charaters_MR1(source_test_case)
        min_value = ord(range_character_set.replace('[', '').replace(']', '').split('-')[0])
        max_value = ord(range_character_set.replace('[', '').replace(']', '').split('-')[1])
        valid_asc_characters = [e for e in range(min_value, max_value + 1)]

        shuffle(valid_asc_characters)

        valid_characters = [chr(item) for item in valid_asc_characters]
        modified_character_set = ''.join(ele for ele in valid_characters)
        modified_character_set = '[' + modified_character_set + ']'
        follow_up_test_case = source_test_case.replace(range_character_set, modified_character_set)
        return follow_up_test_case

    def verify_results(self, output_source, output_follow):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        return self.mr_utl.verify_equal(output_source, output_follow)


"""
the implemention of MR2
"""


class MR2(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR2
        :param source_test_case:
        :return: follow-up test case
        """

        # 获取范围集合
        range_character_set = self.mr_utl.get_range_charaters_MR1(source_test_case)
        min_value = ord(range_character_set.replace('[', '').replace(']', '').split('-')[0])
        max_value = ord(range_character_set.replace('[', '').replace(']', '').split('-')[1])

        valid_asc_characters = [e for e in range(min_value, max_value + 1)]

        shuffle(valid_asc_characters)

        valid_characters = [chr(item) for item in valid_asc_characters]

        modified_character_set = '|'.join(ele for ele in valid_characters)
        follow_up_test_case = source_test_case.replace(range_character_set, modified_character_set)

        return follow_up_test_case

    def verify_results(self, output_source, output_follow):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        return self.mr_utl.verify_equal(output_source, output_follow)


"""
the implemention of MR3
"""


class MR3(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case
        """
        # 获取范围集合
        range_character_set = self.mr_utl.get_collection_characters_MR3(source_test_case)

        new_character = ['[' + ele + ']' for ele in range_character_set.replace('[', '').replace(']', '')]
        new_case = '|'.join(ele for ele in new_character)

        follow_up_test_case = source_test_case.replace(range_character_set, new_case)
        return follow_up_test_case

    def verify_results(self, output_source, output_follow):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        return self.mr_utl.verify_equal(output_source, output_follow)


"""
the implemention of MR4
"""


class MR4(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case
        """
        # 获取范围集合字符串
        old_range_character_set_str = self.mr_utl.get_range_charaters_MR1(source_test_case)

        # 获得最小、中间和最大的ＡＳＣＩＩ码值
        min_asc = ord(old_range_character_set_str.replace('[', '').replace(']', '').split('-')[0])
        middle_asc = min_asc + 1
        max_asc = ord(old_range_character_set_str.replace('[', '').replace(']', '').split('-')[1])
        new_range_character_set_str = '[' + chr(min_asc) + '-' + chr(middle_asc) + ']|[' + \
                                      chr(middle_asc + 1) + '-' + chr(max_asc) + ']'

        return source_test_case.replace(old_range_character_set_str, new_range_character_set_str)

    def verify_results(self, output_source, output_follow):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        return self.mr_utl.verify_equal(output_source, output_follow)


"""
the implemention of MR5
"""


class MR5(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case
        """
        new_order = [c1 for c1 in source_test_case]
        shuffle(new_order)
        return '[' + ''.join(c for c in new_order) + ']'

    def verify_results(self, output_source, output_follow):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        return self.mr_utl.verify_appertain(output_source, output_follow)


"""
the implemention of MR6
"""


class MR6(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case
        """
        new_order = [c1 for c1 in source_test_case]
        shuffle(new_order)
        return '|'.join(c for c in new_order)

    def verify_results(self, output_source, output_follow):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        return self.mr_utl.verify_appertain(output_source, output_follow)


"""
the implemention of MR7
"""


class MR7(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case
        """
        # 获取范围集合
        old_range_character_set_str = self.mr_utl.get_range_charaters_MR1(source_test_case)
        # 获得最大和最小的ａｓｃＩＩ码值
        min_asc = ord(old_range_character_set_str.replace('[', '').replace(']', '').split('-')[0])
        max_asc = ord(old_range_character_set_str.replace('[', '').replace(']', '').split('-')[1])
        middle_asc = max_asc - 1
        new_range_character_set_str = '[' + chr(min_asc) + '-' + chr(middle_asc) + ']'

        return source_test_case.replace(old_range_character_set_str, new_range_character_set_str)

    def verify_results(self, output_source, output_follow):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        return self.mr_utl.verify_includ(output_source, output_follow)


"""
the implemention of MR8
"""


class MR8(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case
        """
        # 获取范围集合
        old_range_character_set_str = self.mr_utl.get_range_charaters_MR1(source_test_case)
        # 获得最大和最小的ａｓｃＩＩ码值
        min_asc = ord(old_range_character_set_str.replace('[', '').replace(']', '').split('-')[0])
        max_asc = ord(old_range_character_set_str.replace('[', '').replace(']', '').split('-')[1])
        new_max_asc = max_asc + 1
        new_range_character_set_str = '[' + chr(min_asc) + '-' + chr(new_max_asc) + ']'

        return source_test_case.replace(old_range_character_set_str, new_range_character_set_str)

    def verify_results(self,output_source, output_follow):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        return self.mr_utl.verify_appertain(output_source, output_follow)


"""
the implemention of MR9
"""


class MR9(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case: 在source_test_case的基础上增加"|[[:digit:]]"
        """
        return source_test_case + "|[[:digit:]]"

    def verify_results(self, output_source, output_follow):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        return self.mr_utl.verify_result_MR9(output_source, output_follow)


"""
the implemention of MR10
"""


class MR10(MR):
    mr_utl = MyUtl()
    tool = Utl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR3
        :param source_test_case:
        :return: follow-up test case
        """
        candidate_literals = ['{1}', '+']

        normal_literals_path = os.path.join(os.path.abspath('.'), 'mapping relation',
                                            'normal_literals')
        if not os.path.exists(normal_literals_path):
            print('此路径不存在：'+normal_literals_path)
            exit()
        normal_literals = linecache.getline(normal_literals_path, int(source_test_case_index)).strip()

        new_normal_literals = normal_literals + candidate_literals[random.randint(0, 1)]

        return source_test_case.replace(normal_literals, new_normal_literals)

    def verify_results(self, output_source, output_follow):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        return self.mr_utl.verify_equal(output_source, output_follow)


"""
the implemention of MR11
"""


class MR11(MR):
    mr_utl = MyUtl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        accept source test case and generate follow-up test case according to the MR11
        :param source_test_case:
        :return:
        """
        a_dict = dict()
        a_dict['\w'] = '\W'
        a_dict['\W'] = '\w'
        a_dict['[[:alnum:]]'] = '[^[:alnum:]]'
        a_dict['[^[:alnum:]]'] = '[[:alnum:]]'
        valid_choices = ['\w', '\W', '[[:alnum:]]', '[^[:alnum:]]']

        old_value = ''
        new_value = ''

        for index in range(0, len(valid_choices)):
            if valid_choices[index] in source_test_case:
                old_value = valid_choices[index]
                new_value = a_dict[valid_choices[index]]
                break
        follow_test_case = source_test_case.replace(old_value, new_value)

        return follow_test_case

    def verify_results(self, output_source, output_follow):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """

        pass

    def verify_MR11_results(self, input_index, output_source, output_follow):
        """
        由于该ＭＲ需要特定的目标文件才能验证测试结果，因此需要目标问津的编号，该编号对应测试用例的编号
        :param repetitive_index:　重复试验的额编号
        :param testing_index:　测试编号
        :param test_case_index:　测试用例的编号
        :return:　是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """

        return self.mr_utl.verify_result_MR11(input_index, output_source, output_follow)


"""
the implemention of MR12
"""


class MR12(MR):
    mr_utl = MyUtl()
    tool = Utl()

    def generate_follow_test_case(self, source_test_case, source_test_case_index):
        """
        将source_test_case中的正常字符添加...，本文为了方便将所有的正常字符转化为"..."
        ＠source_test_case: 原始测试用例
        ＠source_test_case_index原始测试用例的编号，在ＭＲＸ文件中对应一行测试用例的最前面的数字，例如：
        1:only：１就是source_test_case_index的编号，only为实际的测试用例
        @return: 衍生测试用例
        """
        # 获取原始测试用例中的正常字符
        normal_literals_path = os.path.join(os.path.abspath('.'), 'mapping relation',
                                            'normal_literals')
        if not os.path.exists(normal_literals_path):
            print('此路径不存在：'+normal_literals_path)
            exit()
        normal_literal = self.tool.get_line_content(normal_literals_path, int(source_test_case_index))

        new_normal_literal = ''
        for i in range(0, len(normal_literal)):
            new_normal_literal += '.'

        return source_test_case.replace(normal_literal, new_normal_literal)

    def verify_results(self, output_source, output_follow):
        """
        验证原始测试用例与衍生测试用例的执行结果
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        return self.mr_utl.verify_appertain(output_source, output_follow)


class MR_factory(object):
    """
    蜕变关系工厂，根据ＭＲ的名字返回相应的对象
    """

    def choose_MR(self, MR_name):
        if MR_name == 'MR1':
            return MR1()
        elif MR_name == 'MR2':
            return MR2()
        elif MR_name == 'MR3':
            return MR3()
        elif MR_name == 'MR4':
            return MR4()
        elif MR_name == 'MR5':
            return MR5()
        elif MR_name == 'MR6':
            return MR6()
        elif MR_name == 'MR7':
            return MR7()
        elif MR_name == 'MR8':
            return MR8()
        elif MR_name == 'MR9':
            return MR9()
        elif MR_name == 'MR10':
            return MR10()
        elif MR_name == 'MR11':
            return MR11()
        else:
            return MR12()

    def verify_result_no_MR11(self, MR_name, output_source, output_follow):
        if MR_name == 'MR1':
            return MR1().verify_results(output_source, output_follow)
        elif MR_name == 'MR2':
            return MR2().verify_results(output_source, output_follow)
        elif MR_name == 'MR3':
            return MR3().verify_results(output_source, output_follow)
        elif MR_name == 'MR4':
            return MR4().verify_results(output_source, output_follow)
        elif MR_name == 'MR5':
            return MR5().verify_results(output_source, output_follow)
        elif MR_name == 'MR6':
            return MR6().verify_results(output_source, output_follow)
        elif MR_name == 'MR7':
            return MR7().verify_results(output_source, output_follow)
        elif MR_name == 'MR8':
            return MR8().verify_results(output_source, output_follow)
        elif MR_name == 'MR9':
            return MR9().verify_results(output_source, output_follow)
        elif MR_name == 'MR10':
            return MR10().verify_results(output_source, output_follow)
        elif MR_name == 'MR12':
            return MR12().verify_results(output_source, output_follow)
        else:
            pass

    def verify_MR11_result(self, input_index, output_source, output_follow):
        return MR11().verify_MR11_results(input_index, output_source, output_follow)


if __name__ == '__main__':
    mr = MR10()
    print(mr.generate_follow_test_case(r"usr/bin/nohup?", '223'))
    # print(mr.verify_results('mutant1', '1'))

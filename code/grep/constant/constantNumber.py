#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/10/28
# @Anthor   : phantomDai
"""
this script includes some constant
"""
import os

# the path of the partition dir
partition_dir_path = os.path.join(os.path.abspath('..'), 'partition')

mapping_relation_dir_path = os.path.join(os.path.abspath('..'), 'mapping relation')


# 测试用例与蜕变关系的映射关系
test_cases_2_mrs_path = os.path.join(os.path.abspath('.'), 'mapping relation', 'testcase_2_MRs')

# 所有的变异体的名称
mutant_names_list = ['grep_v1', 'grep_v2', 'grep_v3', 'grep_v4', 'grep_v5', 'grep_v6', 'grep_v7', 'grep_v8',
                     'grep_v9', 'grep_v10', 'grep_v11', 'grep_v12', 'grep_v13', 'grep_v14', 'grep_v15',
                     'grep_v16', 'grep_v17', 'grep_v18', 'grep_v19', 'grep_v20']
# mutant_names_list = ['grep_v2', 'grep_v4', 'grep_v6', 'grep_v13', 'grep_v15','grep_v17', 'grep_v18', 'grep_v19']

partition_scheme_path = os.path.join(partition_dir_path, 'partition_scheme')


partition_scheme_testframes_path = os.path.join(partition_dir_path, 'partition_scheme_testframes_1.2')

partition_scheme_testcases_file_path = os.path.join(partition_dir_path, 'partition_scheme_testcases_file')

partition_map_file_path = os.path.join(partition_dir_path, 'partition_map_file')


test_frame_file_path = os.path.join(partition_dir_path, 'partition_scheme_testframes_1.2')

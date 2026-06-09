# from MRs import *
import os
import random

random.seed(1)


class TestCase:
    def __init__(self):
        pass

    def setInputOutput(self, input_name, output_name):
        self.input = input_name
        self.output = output_name


if __name__ == "__main__":
    firstdir = '../../data/PT/inputs/'  # 要复制文件所在路径
    tardir = '../../data/PT/input/'  # 想要复制到的路径
    pathdir = os.listdir(firstdir)  # 获取所在路径下的所有文件
    path = []
    for name in pathdir:
        path.append(firstdir + name)
    sample = random.sample(path, 1000)
    # sample[0] = 'D:/程序/博士/MT/P1/Siemens-suite-master/printtokens/inputs/newtst552.tst'
    for i in range(len(path)):
        # shutil.copyfile(sample[i], tardir + "input{}.txt".format(i))  # 复制操作
        file = open(path[i], 'r')
        lines = file.readlines()
        with open(tardir + "input{}".format(i), "w") as f:
            f.writelines(lines)


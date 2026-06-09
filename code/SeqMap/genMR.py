import random
import os
from typing import List

class I:
    def __init__(self, e: int = 3, T: List[str] = None, p: str = ''):
        self.e = e
        self.T = T if T is not None else []
        self.p = p

    def __eq__(self, other):
        return self.e == other.e and self.p == other.p and self.T == other.T

    def __ne__(self, other):
        return not self.__eq__(other)

class O:
    def __init__(self):
        self.M = []

def random_ll(m):
    return random.randint(0, m - 1)

def random_range(l, r):
    return random.randint(l, r)

def MR1(sourceI: I) -> I:
    followI = I(sourceI.e, list(sourceI.T), sourceI.p)
    nT = len(sourceI.T)
    selected = list(range(nT))
    random.shuffle(selected)
    nSelected = random_range(1, nT)
    for i in range(nSelected):
        followI.p += followI.T[selected[i]]
    return followI

MIN_E_N = 0
MAX_E_N = 4

def MR2(sourceI: I) -> I:
    if sourceI.e == MIN_E_N or sourceI.e == MAX_E_N:
        return sourceI
    followI = I(sourceI.e, list(sourceI.T), sourceI.p)
    followI.e = (followI.e + random_range(1, 4)) % 5
    return followI

def MR3(sourceI: I) -> I:
    followI = I(sourceI.e, list(sourceI.T), sourceI.p)
    lenP = len(followI.p)
    if lenP < 2:
        return followI
    lenCut = random_range(1, lenP - 1)
    if random.randint(0, 1):
        followI.p = followI.p[lenCut:]
    else:
        followI.p = followI.p[:lenP - lenCut]
    lenP = len(followI.p)
    if lenP < 4: # 小于4的话会报错，所以保持原始测试用例不变
        followI = I(sourceI.e, list(sourceI.T), sourceI.p)
        return followI
    return followI

MRs = [MR1, MR2, MR3]

def MR(iMR: int, input: I) -> I:
    assert 1 <= iMR <= len(MRs)
    return MRs[iMR - 1](input)

def read_all(filename: str) -> str:
    with open(filename, 'r') as file:
        return ''.join(file.readlines())

def read_p(filename: str) -> str:
    with open(filename, 'r') as file:
        file.readline()
        return file.readline().strip()

def write_p(filename: str, p: str):
    with open(filename, 'w') as file:
        file.write(">1\n" + p + "\n")

def read_T(filename: str) -> List[str]:
    T = []
    with open(filename, 'r') as file:
        while True:
            label = file.readline()
            if not label:
                break
            line = file.readline()
            if not line:
                break
            T.append(line.strip())
    return T

def write_T(filename: str, T: List[str]):
    with open(filename, 'w') as file:
        for i, t in enumerate(T):
            file.write(f">{i+1}\n{t}\n")

def print_I(i: I, pre: str):
    print(f"{pre}e = {i.e}")
    print(f"{pre}T = [")
    for iT, t in enumerate(i.T):
        print(f"{pre}      {t}{',' if iT != len(i.T)-1 else ' ]'}")
    print(f"{pre}p = {i.p}")

# 调用处理函数
project = 'EMS'
string = 'SeqMap'
path = '../../data/MT/'+project+'/' + string + '/'
input_path = path + "source/e"
output_path = path + "follow/e"
e = []
T = []
p = []
with open(input_path, "r") as fin, open(output_path, 'w') as outfile:
    for line in fin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 3:
            print(f"格式错误：{line}")
            continue
        _, e1, id = parts
        x = int(e1)
        e.append(x)  # 原始行 + 解析后的x值
        T1 = read_T(path + "source/T/{}".format(int(id)))
        T.append(T1)
        p1 = read_p(path + "source/p/{}".format(int(id)))
        p.append(p1)
        sourceI = I(x, T1, p1)
        for iMR, MR in enumerate(MRs, start=1):
            follows = MR(sourceI)
            write_p(path + "follow/p/{}_{}".format(int(id), iMR), follows.p)
            write_T(path + "follow/T/{}_{}".format(int(id), iMR), follows.T)
            output_line = f"f_{iMR} {follows.e} {id} \n"
            outfile.write(output_line)

import math
import random

class I:
    def __init__(self, x):
        self.x = x

class O:
    def __init__(self, y):
        self.y = y  # pi(x)

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# MR 1
def MR1(sourceI, sourceO):
    follow = I(sourceI.x + random.randint(1, 99))
    return [follow]

# MR 2
def MR2(sourceI, sourceO):
    follow = I(sourceI.x + 1)
    return [follow]

# MR 3
def MR3(sourceI, sourceO):
    if sourceI.x < 2:
        return []
    y = max(2, random.randint(1, sourceI.x))
    followXY = I(sourceI.x + y)
    followY = I(y)
    return [followXY, followY]

MRs = [MR1, MR2, MR3]

def pi(x):
    return sum(1 for i in range(2, x + 1) if is_prime(i))

# 读取输入池文件，生成派生输入并写入输出文件
def process_test_pool(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        index = 1
        for line in infile:
            if not line.strip():
                continue
            print(f"[Test {index}] Processing line: {line.strip()}")
            parts = line.strip().split()
            scheme, id_, x = parts[0], parts[1], int(parts[2])
            sourceI = I(x)
            sourceO = O(pi(x))  # 调用 pi(x) 模拟输出

            for iMR, MR in enumerate(MRs, start=1):
                follows = MR(sourceI, sourceO)
                for follow in follows:
                    output_line = f"f_{iMR} {id_} {follow.x}\n"
                    outfile.write(output_line)
            index += 1

# 调用处理函数
project = 'EMS'
string = 'PrimeCount'
path = '../../data/MT/'+project+'/' + string + '/'
process_test_pool(path+"sourceinput", path+"followupinput")

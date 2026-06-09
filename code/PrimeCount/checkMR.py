import math
import json

class I:
    def __init__(self, x: int):
        self.x = x


class O:
    def __init__(self, y: int):
        self.y = y


class Case:
    def __init__(self, i: I, o: O):
        self.i = i
        self.o = o


def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def pi(x: int) -> int:
    return sum(1 for i in range(2, x + 1) if is_prime(i))


# ------------------- MR Rules -------------------

def MR1(source: Case, follows: list[Case], original_source: Case, original_follows: list[Case]) -> int:
    assert len(follows) == 1
    if source.o.y <= follows[0].o.y:
        if original_source.o.y == source.o.y and original_follows[0].o.y == follows[0].o.y:
            return 0
        else:
            return 3 # 假满足
    else:
        return 1 # 1代表违反MR


def MR2(source: Case, follows: list[Case], original_source: Case, original_follows: list[Case]) -> int:
    assert len(follows) == 1
    f = follows[0]
    if source.o.y == f.o.y - (1 if is_prime(f.i.x) else 0):
        if original_source.o.y == source.o.y and original_follows[0].o.y == follows[0].o.y:
            return 0
        else:
            return 3 # 假满足
    else:
        return 1 # 1代表违反MR


def MR3(source: Case, follows: list[Case], original_source: Case, original_follows: list[Case]) -> int:
    assert len(follows) == 2
    if source.o.y >= follows[0].o.y - follows[1].o.y:
        if (original_source.o.y == source.o.y and
                original_follows[0].o.y == follows[0].o.y and original_follows[1].o.y == follows[1].o.y) :
            return 0
        else:
            return 3 # 假满足
    else:
        return 1 # 1代表违反MR


MRs = [MR1, MR2, MR3]


def check_mr(iMR: int, source: Case, follows: list[Case], original_source: Case, original_follows: list[Case]) -> int:
    assert 1 <= iMR <= len(MRs)
    result = MRs[iMR - 1](source, follows, original_source, original_follows)
    return result

# ------------------- 使用示例 -------------------

def run_demo():
    # MR1 示例：source x=10, follow x=15
    source = Case(I(10), O(pi(10)))           # pi(10) = 4
    follow = Case(I(15), O(pi(15)))           # pi(15) = 6
    ok = check_mr(1, source, [follow])
    print("MR1 valid?" , ok)

    # MR2 示例：x=11, x+1=12 (12不是质数)
    src = Case(I(11), O(pi(11)))              # pi(11) = 5
    f2 = Case(I(12), O(pi(12)))               # pi(12) = 5
    print("MR2 valid?", check_mr(2, src, [f2]))

    # MR3 示例：x=10, y=5 => x+y=15
    src = Case(I(10), O(pi(10)))
    fx = Case(I(15), O(pi(15)))
    fy = Case(I(5), O(pi(5)))
    print("MR3 valid?", check_mr(3, src, [fx, fy]))


project = 'EMS'
string = 'PrimeCount'
MG = []
pathsi = '../../data/MT/' + project + '/' + string + '/sourceinput'
pathfi = '../../data/MT/' + project + '/' + string + '/followupinput'
inputsource = []
with open(pathsi, "r") as fin:
    for line in fin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 3:
            print(f"格式错误：{line}")
            continue
        _, id, x_str = parts
        x = int(x_str)
        inputsource.append(x)  # 原始行 + 解析后的x值
inputfollow = []
with open(pathfi, "r") as fin:
    for line in fin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 3:
            print(f"格式错误：{line}")
            continue
        _, id, x_str = parts
        x = int(x_str)
        inputfollow.append(x)  # 原始行 + 解析后的x值

pathso = '../../data/MT/' + project + '/' + string + '/sourceoutput_v0'
pathfo= '../../data/MT/' + project + '/' + string + '/followupoutput_v0'
originalsource = []
with open(pathso, "r") as fin:
    for line in fin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        x_str = parts[0]
        x = int(x_str)
        originalsource.append(x)  # 原始行 + 解析后的x值
originalfollow = []
with open(pathfo, "r") as fin:
    for line in fin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        x_str = parts[0]
        x = int(x_str)
        originalfollow.append(x)  # 原始行 + 解析后的x值

num_mu = 17
for mu in range(num_mu+1):
    MG2 = []
    pathso = '../../data/MT/' + project + '/' + string + '/sourceoutput_v{}'.format(mu)
    pathfo= '../../data/MT/' + project + '/' + string + '/followupoutput_v{}'.format(mu)
    outputsource = []
    with open(pathso, "r") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            x_str = parts[0]
            x = int(x_str)
            outputsource.append(x)  # 原始行 + 解析后的x值
    outputfollow = []
    with open(pathfo, "r") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            x_str = parts[0]
            x = int(x_str)
            outputfollow.append(x)  # 原始行 + 解析后的x值
    for i in range(100):
        so = outputsource[i]
        si = inputsource[i]
        f1o = outputfollow[i * 4]
        f1i = inputfollow[i * 4]
        f2o = outputfollow[i*4 + 1]
        f2i = inputfollow[i * 4 + 1]
        f3xo = outputfollow[i*4 + 2]
        f3xi = inputfollow[i * 4 + 2]
        f3yo = outputfollow[i*4 + 3]
        f3yi = inputfollow[i * 4 + 3]
        source = Case(I(si),O(so))
        follow1 = Case(I(f1i), O(f1o))
        follow2 = Case(I(f2i), O(f2o))
        follow3x = Case(I(f3xi), O(f3xo))
        follow3y = Case(I(f3yi), O(f3yo))
        original_so = originalsource[i]
        original_si = inputsource[i]
        original_f1o = originalfollow[i * 4]
        original_f1i = inputfollow[i * 4]
        original_f2o = originalfollow[i*4 + 1]
        original_f2i = inputfollow[i * 4 + 1]
        original_f3xo = originalfollow[i*4 + 2]
        original_f3xi = inputfollow[i * 4 + 2]
        original_f3yo = originalfollow[i*4 + 3]
        original_f3yi = inputfollow[i * 4 + 3]
        original_source = Case(I(original_si),O(original_so))
        original_follow1 = Case(I(original_f1i), O(original_f1o))
        original_follow2 = Case(I(original_f2i), O(original_f2o))
        original_follow3x = Case(I(original_f3xi), O(original_f3xo))
        original_follow3y = Case(I(original_f3yi), O(original_f3yo))
        MG3 = [check_mr(1, source, [follow1], original_source, [original_follow1])]
        MG3.append(check_mr(2, source, [follow2], original_source, [original_follow2]))
        MG3.append(check_mr(3, source, [follow3x , follow3y], original_source,
                            [original_follow3x , original_follow3y]))
        MG2.append(MG3)
        # data = {
        #          'MGS': MG2
        # }
        # json_str = json.dumps(data)
        # with open('../../data/MT/' + project + '/' + string + '/mutant' + str(mu) + '.json',
        #           'w') as f:
        #     json.dump(json_str, f)
        with open('../../data/MT/' + project + '/' + string + '/mutant' + str(mu) + '.json',
                  'r') as load_f:
            data = json.load(load_f)
        data = json.loads(data)
        data['MGS'] = MG2
        json_str = json.dumps(data)
        with open('../../data/MT/' + project + '/' + string + '/mutant' + str(mu) + '.json',
                  'w') as f:
            json.dump(json_str, f)
    MG.append(MG2)


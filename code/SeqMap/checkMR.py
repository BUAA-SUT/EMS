import os
import sys
from typing import List
from dataclasses import dataclass
import itertools
import subprocess
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))

@dataclass
class I:
    e: int
    T: List[str]
    p: str

    def __eq__(self, other):
        return self.e == other.e and self.T == other.T and self.p == other.p

    def __ne__(self, other):
        return not self.__eq__(other)


@dataclass
class O:
    M: List[int]


@dataclass
class Case:
    i: I
    o: O


def belong(l: List[int], r: List[int]) -> bool:
    return set(l).issubset(set(r))


# def belong(l: List[int], r: List[int], subset=False) -> bool:
#     if len(l) > len(r) or (subset and len(l) == len(r)):
#         return False
#     return sorted(l) == sorted(r[:len(l)])


def MR1(source: Case, follows: List[Case], sourceoutput: Case, followsoutput: List[Case]) -> int:
    assert len(follows) == 1
    follow = follows[0]
    result = belong(source.o.M, follow.o.M)
    if result:
        if source.o.M == sourceoutput.o.M and follow.o.M == followsoutput[0].o.M:
            return 0
        else:
            return 3
    else:
        return 1


def MR2(source: Case, follows: List[Case], sourceoutput: Case, followsoutput: List[Case]) -> int:
    assert len(follows) == 1
    follow = follows[0]
    if source.i.e < follow.i.e:
        result = belong(source.o.M, follow.o.M)
        if result:
            if source.o.M == sourceoutput.o.M and follow.o.M == followsoutput[0].o.M:
                return 0
            else:
                return 3
        else:
            return 1
    else:
        result = belong(follow.o.M, source.o.M)
        if result:
            if source.o.M == sourceoutput.o.M and follow.o.M == followsoutput[0].o.M:
                return 0
            else:
                return 3
        else:
            return 1


def MR3(source: Case, follows: List[Case], sourceoutput: Case, followsoutput: List[Case]) -> int:
    assert len(follows) == 1
    follow = follows[0]
    result = belong(follow.o.M, source.o.M)
    if result:
        if source.o.M == sourceoutput.o.M and follow.o.M == followsoutput[0].o.M:
            return 0
        else:
            return 3
    else:
        return 1


MRs = [MR1, MR2, MR3]


def MR(iMR: int, source: Case, follows: List[Case], sourceoutput: Case, followsoutput: List[Case]) -> int:
    assert 1 <= iMR <= len(MRs)
    return MRs[iMR - 1](source, follows, sourceoutput, followsoutput)


def read_all(filename: str) -> str:
    with open(filename, 'r') as file:
        return ''.join(file.readlines())


def read_p(filename: str) -> str:
    with open(filename, 'r') as file:
        file.readline()  # skip first line
        return file.readline().strip()


def read_T(filename: str) -> List[str]:
    T = []
    with open(filename, 'r') as file:
        while True:
            file.readline()  # skip line
            line = file.readline()
            if not line:
                break
            T.append(line.strip())
    return T


def read_M(filename: str) -> List[int]:
    M = []
    with open(filename, 'r') as file:
        for line in file:
            if "运行失败" in line:
                M.append("运行失败")
                return M
            if 'NM' not in line:  # 如果不是未匹配（即匹配上了）
                parts = line.strip().split()
                if parts:
                    M.append(int(parts[0]))  # 添加编号（行号）作为整数
    return M


if __name__ == "__main__":
    # ✅ 手动指定输入数据路径
    project = 'EMS'
    string = 'SeqMap'
    source_path = '../../data/MT/' + project + '/' + string + '/source/'
    source_e_path = source_path + "e"
    source_p_path = source_path + "p"
    source_T_path = source_path + "T"
    follow_path = '../../data/MT/' + project + '/' + string + '/follow/'
    follow_e_path = follow_path + "e"
    follow_p_path = follow_path + "p"
    follow_T_path = follow_path + "T"
    source_E = []
    follow_E = []
    Id = []
    with open(source_e_path, "r") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 3:
                print(f"格式错误：{line}")
                continue
            _, x_str, id = parts
            x = int(x_str)
            source_E.append(x)  # 原始行 + 解析后的x值
            Id.append(int(id))
    with open(follow_e_path, "r") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 3:
                print(f"格式错误：{line}")
                continue
            _, x_str, id = parts
            x = int(x_str)
            follow_E.append(x)  # 原始行 + 解析后的x值

    MG = []
    Result = []
    num_nu = 5
    for mu in range(1, num_nu+1):
        if mu == 3:
            continue
        MG2 = []
        r2 = []
        for i in range(len(source_E)):
            MG3 = []
            r3 = []
            # ✅ 源用例信息
            source = Case(
                I(source_E[i],
                  read_T(f"{source_T_path}/{str(Id[i])}"),
                  read_p(f"{source_p_path}/{str(Id[i])}")),
                O(read_M(f"{source_path}output_{str(mu)}_{str(Id[i])}"))
            )
            sourceoutput = Case(
                I(source_E[i],
                  read_T(f"{source_T_path}/{str(Id[i])}"),
                  read_p(f"{source_p_path}/{str(Id[i])}")),
                O(read_M(f"{source_path}output_0_{str(Id[i])}"))
            )
            original = read_all(f"{source_path}output_{str(0)}_{str(Id[i])}")
            mutant = read_all(f"{source_path}output_{str(mu)}_{str(Id[i])}")
            if original == mutant:
                r3.append(0)
            elif "运行失败" in mutant:
                r3.append(-1)
            else:
                r3.append(1)
            for j in range(3): # 3个MR
                # ✅ follow-up 用例信息（可多个）
                follow_ids = [str(Id[i])]  # 可以添加多个 ID
                follows = []
                followsoutput = []
                for fid in follow_ids:
                    follow_e = follow_E[i*3+j]
                    follows.append(Case(
                        I(follow_e,
                          read_T(f"{follow_T_path}/{str(Id[i])}_{str(j+1)}"),
                          read_p(f"{follow_p_path}/{str(Id[i])}_{str(j+1)}")),
                        O(read_M(f"{follow_path}output_{str(mu)}_{str(Id[i])}_{str(j+1)}"))
                    ))
                for fid in follow_ids:
                    follow_e = follow_E[i*3+j]
                    followsoutput.append(Case(
                        I(follow_e,
                          read_T(f"{follow_T_path}/{str(Id[i])}_{str(j+1)}"),
                          read_p(f"{follow_p_path}/{str(Id[i])}_{str(j+1)}")),
                        O(read_M(f"{follow_path}output_0_{str(Id[i])}_{str(j+1)}"))
                    ))
                original = read_all(f"{follow_path}output_{str(0)}_{str(Id[i])}_{str(j+1)}")
                mutant = read_all(f"{follow_path}output_{str(mu)}_{str(Id[i])}_{str(j+1)}")
                if original == mutant:
                    r3.append(0)
                elif "运行失败" in mutant:
                    r3.append(-1)
                else:
                    r3.append(1)
                # ✅ 检查 MR 是否成立
                result = MR(j+1, source, follows, sourceoutput, followsoutput)
                MG3.append(result)
            MG2.append(MG3)
            r2.append(r3)
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
        Result.append(r2)

    # result = []
    # for i in range(1):
    #     original = read_all(f"../SeqMap/Mutants/allMutants/seqmap_v0/output.txt")
    #     mutant = read_all(f"../SeqMap/Mutants/allMutants/seqmap_v{i}/output.txt")
    #     if original == mutant:
    #         result.append(0)
    #     else:
    #         result.append(1)

    # Result = []
    # num_nu = 5
    # for mu in range(num_nu+1):
    #     MG2 = []
    #     r2 = []
    #     for i in range(len(source_E)):
    #         r3 = []
    #         # ✅ 源用例信息
    #         source = Case(
    #             I(source_E[i],
    #               read_T(f"{source_T_path}/{str(Id[i])}"),
    #               read_p(f"{source_p_path}/{str(Id[i])}")),
    #             O(read_M(f"{source_path}output_{str(mu)}_{str(Id[i])}"))
    #         )
    #         original = read_all(f"{source_path}output_{str(0)}_{str(Id[i])}")
    #         mutant = read_all(f"{source_path}output_{str(mu)}_{str(Id[i])}")
    #         if original == mutant:
    #             r3.append(0)
    #         elif "运行失败" in mutant:
    #             r3.append(-1)
    #         else:
    #             r3.append(1)
    #         r2.append(r3)
    #     Result.append(r2)

    # mutant_folder = "./Mutants/seqmap_v5"
    # source_file = os.path.join(mutant_folder, "seqmap.cpp")
    # executable = os.path.join(mutant_folder, "seqmap")
    # for file in os.listdir("."):
    #     if file.endswith(".gcda") or file.endswith(".gcov"):
    #         os.remove(file)
    # compile_options = ["clang++", "-fprofile-arcs", "-ftest-coverage","-O0","-g","-o", executable, source_file]
    # # 执行编译程序并将标准错误输出重定向到空设备文件中
    # try:
    #     output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
    # except subprocess.CalledProcessError as e:
    #     output = e.output
    #     print("input编译失败，错误信息：", output.decode())
    # else:
    #     pass
    # command = [executable, str(2), os.path.join(mutant_folder, "probes.fa"), os.path.join(mutant_folder, "trans.fa"),
    #            os.path.join(mutant_folder, "output.txt")]
    # try:
    #     process = subprocess.Popen(
    #         command,
    #         stdin=subprocess.PIPE,
    #         stdout=subprocess.PIPE,
    #         stderr=subprocess.PIPE
    #     )
    #     try:
    #         output, error = process.communicate(timeout=30)
    #         # print("程序输出为：", output.decode())
    #     except subprocess.TimeoutExpired:
    #         process.kill()
    #         print(f"input 超时，命令执行被终止。")
    #         label = 1
    #
    #     if process.returncode != 0:
    #         print(f"input 执行失败，退出码：{process.returncode}")
    #         print("stderr 内容：", repr(error.decode()))
    #         label = 1
    #
    # except Exception as e:
    #     print(f"input 执行过程中发生异常：{e}")
    #     label = 1
    #
    # k = 1  # 获取可执行行
    # gcov_command = ["gcov", "seqmap.cpp"]
    # try:
    #     output = subprocess.check_output(gcov_command)
    # except subprocess.CalledProcessError as e:
    #     output = e.output
    #     print("input命令执行失败，错误信息：", output.decode())
    # else:
    #     print("input命令执行成功，输出信息：", output.decode())

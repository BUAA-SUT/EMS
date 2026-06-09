import csv
import sys
import subprocess
import filecmp
import os
from checkMR import *

# 自动切换工作目录为脚本所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

num_mu = 5
num_case = 100
num_mr = 3

project = 'EMS'
string = 'SeqMap'
source_path = '../../data/MT/'+project+'/' + string + '/source/'
source_e_path = source_path + "e"
source_p_path = source_path + "p"
source_T_path = source_path + "T"
follow_path = '../../data/MT/'+project+'/' + string + '/follow/'
follow_e_path = follow_path + "e"
follow_p_path = follow_path + "p"
follow_T_path = follow_path + "T"


for mu in range(num_mu+1):
    if mu == 3:
        continue
    label = 0
    # 构造路径
    mutant_folder = "./Mutants/seqmap_v{}".format(mu)
    source_file = os.path.join(mutant_folder, "seqmap.cpp")
    executable = os.path.join(mutant_folder, "seqmap")
    statevalue = []
    statetitle = []
    pq = 0
    with open(source_path+ '/statementsource_v{}.csv'.format(mu), 'w') as csvfile1:
        spamwriter1 = csv.writer(csvfile1, delimiter=',')
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
                for file in os.listdir("."):
                    if file.endswith(".gcda") or file.endswith(".gcov"):
                        os.remove(file)
                compile_options = ["clang++", "-fprofile-arcs", "-ftest-coverage","-O0","-g","-o", executable, source_file]
                # 执行编译程序并将标准错误输出重定向到空设备文件中
                try:
                    output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
                except subprocess.CalledProcessError as e:
                    output = e.output
                    print(f"input{id}编译失败，错误信息：", output.decode())
                else:
                    pass
                command = [executable, x_str, source_T_path+"/{}".format(int(id)), source_p_path+"/{}".format(int(id)),
                           source_path + "output_{}_{}".format(mu, int(id))]
                try:
                    process = subprocess.Popen(
                        command,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    try:
                        output, error = process.communicate(timeout=30)
                        # print("程序输出为：", output.decode())
                    except subprocess.TimeoutExpired:
                        process.kill()
                        print(f"input{id} 超时，命令执行被终止。")
                        label = 1
                        break

                    if process.returncode != 0:
                        print(f"input{id} 执行失败，错误信息：{error.decode()}")
                        label = 1
                        break

                except Exception as e:
                    print(f"input{id} 执行过程中发生异常：{e}")
                    label = 1
                    break

                k = 1  # 获取可执行行
                gcov_command = ["gcov", "seqmap.cpp"]
                try:
                    output = subprocess.check_output(gcov_command)
                except subprocess.CalledProcessError as e:
                    output = e.output
                    print(f"input{id}命令执行失败，错误信息：", output.decode())
                else:
                    print(f"input{id}命令执行成功，输出信息：", output.decode())
                    # pass

                statevalue.append(f"input{id}")
                statetitle.append("inputs")

                fp2 = open("seqmap.cpp.gcov")
                for line1 in fp2:
                    try:
                        flag = line1.split(":")[0]
                        flag1 = line1.split(":")[1].strip()
                        if flag1[0] == '0':
                            continue
                        if "-" in flag:
                            k = k + 1
                            continue
                        elif "#####" in flag:
                            statevalue.append("0")
                            statetitle.append(k)
                            k = k + 1
                        else:
                            statevalue.append("1")
                            statetitle.append(k)
                            k = k + 1
                    except:
                        print("exiting")
                        exit(1)

                statetitle.append("Oracle")
                if pq == 0:
                    spamwriter1.writerow(statetitle)
                    pq = 1
                output_original = read_M(f"{source_path}output_{str(0)}_{id}")
                output_mutant = read_M(f"{source_path}output_{str(mu)}_{id}")
                if output_original == output_mutant:
                    statevalue.append(int('0'))
                else:
                    statevalue.append(int('1'))

                if len(statevalue) > 1:
                    spamwriter1.writerow(statevalue)
                    statevalue = []
                    statetitle = []
                else:
                    statevalue = []
                    statetitle = []

                if label == 1:
                    break
        if label == 1:
            continue

    statevalue = []
    statetitle = []
    pq = 0
    with open(follow_path + '/statementfollow_v{}.csv'.format(mu), 'w') as csvfile1:
        spamwriter1 = csv.writer(csvfile1, delimiter=',')
        with open(follow_e_path, "r") as fin:
            for line in fin:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                if len(parts) != 3:
                    print(f"格式错误：{line}")
                    continue
                flag, x_str, id = parts
                mr = flag.split('_')[-1]
                for file in os.listdir("."):
                    if file.endswith(".gcda") or file.endswith(".gcov"):
                        os.remove(file)
                compile_options = ["clang++", "-fprofile-arcs", "-ftest-coverage","-O0","-g","-o", executable, source_file]
                # 执行编译程序并将标准错误输出重定向到空设备文件中
                try:
                    output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
                except subprocess.CalledProcessError as e:
                    output = e.output
                    print(f"input{id}_{mr}编译失败", output.decode())
                else:
                    pass
                command = [executable, x_str, follow_T_path+"/{}_".format(int(id))+mr, follow_p_path+"/{}_".format(int(id))+mr,
                       follow_path + "output_{}_{}_".format(mu, int(id))+mr]
                try:
                    process = subprocess.Popen(
                        command,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    try:
                        output, error = process.communicate(timeout=30)
                        # print("程序输出为：", output.decode())
                    except subprocess.TimeoutExpired:
                        process.kill()
                        print(f"input{id}_{mr} 超时，命令执行被终止。")
                        label = 1
                        break

                    if process.returncode != 0:
                        print(f"input{id}_{mr} 执行失败，错误信息：{error.decode()}")
                        label = 1
                        break

                except Exception as e:
                    print(f"input{id}_{mr} 执行过程中发生异常：{e}")
                    label = 1
                    break

                k = 1  # 获取可执行行
                gcov_command = ["gcov", "seqmap.cpp"]
                try:
                    output = subprocess.check_output(gcov_command)
                except subprocess.CalledProcessError as e:
                    output = e.output
                    print(f"input{id}_{mr}命令执行失败，错误信息：", output.decode())
                else:
                    print(f"input{id}_{mr}命令执行成功，输出信息：", output.decode())
                    # pass

                statevalue.append(f"input{id}_{mr}")
                statetitle.append("inputs")

                fp2 = open("seqmap.cpp.gcov")
                for line1 in fp2:
                    try:
                        flag = line1.split(":")[0]
                        flag1 = line1.split(":")[1].strip()
                        if flag1[0] == '0':
                            continue
                        if "-" in flag:
                            k = k + 1
                            continue
                        elif "#####" in flag:
                            statevalue.append("0")
                            statetitle.append(k)
                            k = k + 1
                        else:
                            statevalue.append("1")
                            statetitle.append(k)
                            k = k + 1
                    except:
                        print("exiting")
                        exit(1)

                statetitle.append("Oracle")
                if pq == 0:
                    spamwriter1.writerow(statetitle)
                    pq = 1
                output_original = read_M(f"{follow_path}output_{str(0)}_{id}_{mr}")
                output_mutant = read_M(f"{follow_path}output_{str(mu)}_{id}_{mr}")
                if output_original == output_mutant:
                    statevalue.append(int('0'))
                else:
                    statevalue.append(int('1'))

                if len(statevalue) > 1:
                    spamwriter1.writerow(statevalue)
                    statevalue = []
                    statetitle = []
                else:
                    statevalue = []
                    statetitle = []
                if label == 1:
                    break
        if label == 1:
            continue


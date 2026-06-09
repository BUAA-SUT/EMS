import csv
import sys
import subprocess
import filecmp
import os

# 自动切换工作目录为脚本所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

num_mu = 29
num_case = 100
num_mr = 3

project = 'EMS'
string = 'PrimeCount'
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
oraclesource = []
with open(pathso, "r") as fin:
    for line in fin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        x_str = parts[0]
        x = int(x_str)
        oraclesource.append(x)
oraclefollow = []
with open(pathfo, "r") as fin:
    for line in fin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        x_str = parts[0]
        x = int(x_str)
        oraclefollow.append(x)

for mutant in range(num_mu+1):
    label = 0
    # 构造路径
    mutant_folder = "./Mutants/PrimeCount_v{}".format(mutant)
    source_file = os.path.join(mutant_folder, "PrimeCount.cpp")
    executable = os.path.join(mutant_folder, "PrimeCount")
    pathso = '../../data/MT/' + project + '/' + string + '/sourceoutput_v{}'.format(mutant)
    pathfo = '../../data/MT/' + project + '/' + string + '/followupoutput_v{}'.format(mutant)
    mutantsource = []
    with open(pathso, "r") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            x_str = parts[0]
            x = int(x_str)
            mutantsource.append(x)
    mutantfollow = []
    with open(pathfo, "r") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            x_str = parts[0]
            x = int(x_str)
            mutantfollow.append(x)
    statevalue = []
    statetitle = []
    pq = 0
    with open('../../data/MT/' + project + '/' + string + '/statementsource_v{}.csv'.format(mutant), 'w') as csvfile1:
        spamwriter1 = csv.writer(csvfile1, delimiter=',')
        for i, input_data in enumerate(inputsource):
            for file in os.listdir("."):
                if file.endswith(".gcda") or file.endswith(".gcov"):
                    os.remove(file)
            compile_options = ["clang++", "-fprofile-arcs", "-ftest-coverage","-o", executable, source_file]
            # 执行编译程序并将标准错误输出重定向到空设备文件中
            try:
                output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                output = e.output
                print("input{}编译失败，错误信息：".format(i), output.decode())
            else:
                pass
            command = [executable, str(input_data)]
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
                    print(f"input{i} 超时，命令执行被终止。")
                    label = 1
                    break

                if process.returncode != 0:
                    print(f"input{i} 执行失败，错误信息：{error.decode()}")
                    label = 1
                    break

            except Exception as e:
                print(f"input{i} 执行过程中发生异常：{e}")
                label = 1
                break

            k = 1  # 获取可执行行
            gcov_command = ["gcov", "PrimeCount.cpp"]
            try:
                output = subprocess.check_output(gcov_command)
            except subprocess.CalledProcessError as e:
                output = e.output
                print("input{}命令执行失败，错误信息：".format(i), output.decode())
            else:
                print("input{}命令执行成功，输出信息：".format(i), output.decode())
                # pass

            statevalue.append("input{}".format(i))
            statetitle.append("inputs")

            fp2 = open("PrimeCount.cpp.gcov")
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

            output_oringinal = oraclesource[i]
            output_mutant = mutantsource[i]
            if output_oringinal == output_mutant:
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

    pq = 0
    with open('../../data/MT/' + project + '/' + string + '/statementfollow_v{}.csv'.format(mutant), 'w') as csvfile1:
        spamwriter1 = csv.writer(csvfile1, delimiter=',')
        for i, input_data in enumerate(inputfollow):
            for file in os.listdir("."):
                if file.endswith(".gcda") or file.endswith(".gcov"):
                    os.remove(file)
            compile_options = ["clang++", "-fprofile-arcs", "-ftest-coverage","-o", executable, source_file]
            # 执行编译程序并将标准错误输出重定向到空设备文件中
            try:
                output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                output = e.output
                print("input{}编译失败，错误信息：".format(i), output.decode())
            else:
                pass
            command = [executable, str(input_data)]
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
                    print(f"input{i} 超时，命令执行被终止。")
                    label = 1
                    break

                if process.returncode != 0:
                    print(f"input{i} 执行失败，错误信息：{error.decode()}")
                    label = 1
                    break

            except Exception as e:
                print(f"input{i} 执行过程中发生异常：{e}")
                label = 1
                break

            k = 1  # 获取可执行行
            gcov_command = ["gcov", "PrimeCount.cpp"]
            try:
                output = subprocess.check_output(gcov_command)
            except subprocess.CalledProcessError as e:
                output = e.output
                print("input{}命令执行失败，错误信息：".format(i), output.decode())
            else:
                print("input{}命令执行成功，输出信息：".format(i), output.decode())
                # pass

            statevalue.append("input{}".format(i))
            statetitle.append("inputs")

            fp2 = open("PrimeCount.cpp.gcov")
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

            output_oringinal = oraclefollow[i]
            output_mutant = mutantfollow[i]
            if output_oringinal == output_mutant:
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
            # for m in range(num_mr):
            #     if os.path.exists("PrimeCount.gcda"):
            #         os.remove("PrimeCount.gcda")
            #     compile_options = ["clang++", "-fprofile-arcs", "-ftest-coverage",
            #                        "Mutants/PrimeCount_v{}/PrimeCount.cpp".format(mutant)]
            #     # 执行编译程序并将标准错误输出重定向到空设备文件中
            #     try:
            #         output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
            #     except subprocess.CalledProcessError as e:
            #         output = e.output
            #         print("input{}_{}编译失败，错误信息：".format(i, m), output.decode())
            #     else:
            #         pass
            #
            #     l1 = '../../data/PT/RandomInput/input{}_{}.txt'.format(i, m)
            #     command = ["./a.out", l1]
            #     try:
            #         # output = subprocess.check_output(command)
            #         timeout_seconds = 30  # 设置超时时间为60秒
            #         # 启动进程
            #         process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #         try:
            #             # 执行命令并设置超时时间
            #             output, error = process.communicate(timeout=timeout_seconds)
            #             # 输出命令执行结果
            #             # print(output.decode("utf-8"))
            #         except subprocess.TimeoutExpired:
            #             # 如果命令超时，结束进程
            #             process.kill()
            #             # 输出超时信息
            #             print("Command execution timeout!")
            #             label = 1
            #             break
            #     except subprocess.CalledProcessError as e:
            #         output = e.output
            #         print("input{}_{}执行失败，输出信息：".format(i, m), output.decode())
            #         label = 1
            #         break
            #     else:
            #         # print("input{}执行成功，输出信息：\n".format(i), output.decode())
            #         pass
            #
            #     k = 1
            #     command = ["gcov", "print_tokens.c"]
            #     try:
            #         output = subprocess.check_output(command)
            #     except subprocess.CalledProcessError as e:
            #         output = e.output
            #         print("input{}_{}命令执行失败，错误信息：".format(i, m), output.decode())
            #     else:
            #         print("input{}_{}命令执行成功，输出信息：\n".format(i, m), output.decode())
            #         # pass
            #
            #     statevalue.append("input{}_{}".format(i, m))
            #     statetitle.append("inputs")
            #
            #     fp2 = open("print_tokens.c.gcov")
            #     for line1 in fp2:
            #         try:
            #             flag = line1.split(":")[0]
            #             flag1 = line1.split(":")[1].strip()
            #             if flag1[0] == '0':
            #                 continue
            #             if "-" in flag:
            #                 k = k + 1
            #                 continue
            #             elif "#####" in flag:
            #                 statevalue.append("0")
            #                 statetitle.append(k)
            #                 k = k + 1
            #             else:
            #                 statevalue.append("1")
            #                 statetitle.append(k)
            #                 k = k + 1
            #         except:
            #             print("exiting")
            #             exit(1)
            #
            #     # for mu in range(1, num_mu+1):
            #     #     statetitle.append("Mutant{}".format(mu))
            #     statetitle.append("Oracle")
            #     if pq == 0:
            #         spamwriter1.writerow(statetitle)
            #         pq = 1
            #     # for mu in range(1, num_mu+1):
            #     output_oringinal = originaloutput["output{}_{}".format(i, m)]
            #     output_mutant = mutateoutput["output{}_{}".format(i, m)]
            #     if output_oringinal == output_mutant:
            #         statevalue.append(int('0'))
            #     else:
            #         statevalue.append(int('1'))
            #     if len(statevalue) > 1:
            #         spamwriter1.writerow(statevalue)
            #         statevalue = []
            #         statetitle = []
            #     else:
            #         statevalue = []
            #         statetitle = []
            #     for n in range(num_mr):
            #         if os.path.exists("print_tokens.gcda"):
            #             os.remove("print_tokens.gcda")
            #         compile_options = ["gcc", "-fprofile-arcs", "-ftest-coverage", "Mutants/printtokens_v{}/print_tokens.c".format(mutant)]
            #         # 执行编译程序并将标准错误输出重定向到空设备文件中
            #         try:
            #             output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
            #         except subprocess.CalledProcessError as e:
            #             output = e.output
            #             print("input{}_{}_{}编译失败，错误信息：".format(i, m, n), output.decode())
            #         else:
            #             pass
            #         l1 = '../../data/PT/RandomInput/input{}_{}_{}.txt'.format(i, m, n)
            #         # os.system("./a.out " + l1)
            #         command = ["./a.out", l1]
            #         try:
            #             # output = subprocess.check_output(command)
            #             timeout_seconds = 30  # 设置超时时间为60秒
            #             # 启动进程
            #             process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #             try:
            #                 # 执行命令并设置超时时间
            #                 output, error = process.communicate(timeout=timeout_seconds)
            #                 # 输出命令执行结果
            #                 # print(output.decode("utf-8"))
            #             except subprocess.TimeoutExpired:
            #                 # 如果命令超时，结束进程
            #                 process.kill()
            #                 # 输出超时信息
            #                 print("Command execution timeout!")
            #                 label = 1
            #                 break
            #         except subprocess.CalledProcessError as e:
            #             output = e.output
            #             print("input{}_{}_{}执行失败，输出信息：".format(i, m, n), output.decode())
            #             label = 1
            #             break
            #         else:
            #             # print("input{}执行成功，输出信息：\n".format(i), output.decode())
            #             pass
            #         k = 1
            #         command = ["gcov", "print_tokens.c"]
            #         try:
            #             output = subprocess.check_output(command)
            #         except subprocess.CalledProcessError as e:
            #             output = e.output
            #             print("input{}_{}_{}命令执行失败，错误信息：".format(i, m, n), output.decode())
            #         else:
            #             print("input{}_{}_{}命令执行成功，输出信息：\n".format(i, m, n), output.decode())
            #             # pass
            #
            #         statevalue.append("input{}_{}_{}".format(i, m, n))
            #         statetitle.append("inputs")
            #
            #         fp2 = open("print_tokens.c.gcov")
            #         for line1 in fp2:
            #             try:
            #                 flag = line1.split(":")[0]
            #                 flag1 = line1.split(":")[1].strip()
            #                 if flag1[0] == '0':
            #                     continue
            #                 if "-" in flag:
            #                     k = k + 1
            #                     continue
            #                 elif "#####" in flag:
            #                     statevalue.append("0")
            #                     statetitle.append(k)
            #                     k = k + 1
            #                 else:
            #                     statevalue.append("1")
            #                     statetitle.append(k)
            #                     k = k + 1
            #             except:
            #                 print("exiting")
            #                 exit(1)
            #
            #         # for mu in range(1, num_mu+1):
            #         #     statetitle.append("Mutant{}".format(mu))
            #         statetitle.append("Oracle")
            #         if pq == 0:
            #             spamwriter1.writerow(statetitle)
            #             pq = 1
            #         # for mu in range(1, num_mu+1):
            #         output_oringinal = originaloutput["output{}_{}_{}".format(i, m, n)]
            #         output_mutant = mutateoutput["output{}_{}_{}".format(i, m, n)]
            #         if output_oringinal == output_mutant:
            #             statevalue.append(int('0'))
            #         else:
            #             statevalue.append(int('1'))
            #         if len(statevalue) > 1:
            #             spamwriter1.writerow(statevalue)
            #             statevalue = []
            #             statetitle = []
            #         else:
            #             statevalue = []
            #             statetitle = []
            #     if label == 1:
            #        break
            if label == 1:
                break
    if label == 1:
        continue


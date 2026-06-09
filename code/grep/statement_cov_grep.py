import csv
import os
import sys
import subprocess
import filecmp
import test_grep


def get_output(mu):
    outputdir1 = '../../data/grep/RandomOutput0.csv'
    outputdir2 = '../../data/grep/RandomOutput{}.csv'.format(mu)
    # outputdir1 = '/home/rdx/data/MT/STVR/grep/TranstoServer/RandomOutput0.csv'
    # outputdir2 = '/home/rdx/data/MT/STVR/grep/TranstoServer/RandomOutput{}.csv'.format(mu)
    csvFile = open(outputdir1, "r")
    reader = csv.reader(csvFile)
    # 建立空字典
    outputcase1 = {}
    for item in reader:
        # 忽略第一行
        if reader.line_num == 1:
            continue
        try:
            outputcase1[item[0]] = item[1]
        except:
            print(item)
            print(reader.line_num)
            break
    csvFile.close()

    csvFile = open(outputdir2, "r")
    reader = csv.reader(csvFile)
    outputcase2 = {}
    for item in reader:
        # 忽略第一行
        if reader.line_num == 1:
            continue
        try:
            outputcase2[item[0]] = item[1]
        except:
            print(item)
            print(reader.line_num)
            break
    csvFile.close()
    return outputcase1, outputcase2


if __name__ == "__main__":
    # Output = []
    # for mu in range(1, 12):
    #     output1, output2 = get_output(mu)
    #     if mu == 1:
    #         Output.append(output1)
    #         Output.append(output2)
    #     else:
    #         Output.append(output2)
    for mutant in range(1, 12):
        # label = 0
        output1, output2 = get_output(mutant)
        statevalue = []
        statetitle = []
        pq = 0
        inputdata = test_grep.get_input()
        # '../../data/grep/statementResult.csv'
        csvfile1 = open('../../data/grep/statementResult{}_1.csv'.format(mutant), 'w')
        spamwriter1 = csv.writer(csvfile1, delimiter=',')
        t = 1
        x = 1
        for i in range(len(output1)):
            if t > 1000:
                x += 1
                t = 1
                pq = 0
                csvfile1 = open('../../data/grep/statementResult{}_{}.csv'.format(mutant, x), 'w')
                spamwriter1 = csv.writer(csvfile1, delimiter=',')
            if os.path.exists("grep.gcda"):
                os.remove("grep.gcda")
            name = list(output1.keys())[i]
            compile_options = ["gcc", "-fprofile-arcs", "-ftest-coverage", "Mutants/grep_v{}/grep.c".format(mutant)]
            # 执行编译程序并将标准错误输出重定向到空设备文件中
            try:
                output = subprocess.check_output(compile_options, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                output = e.output
                print(name+"编译失败，错误信息：", output.decode())
            else:
                pass
            # 判断MR
            last_underscore = name.rfind("_")
            mr = 'MR'+name[last_underscore + 1:]
            if 'source' in name:
                start = name.find('output_source') + len('output_source')
                end = name.find('_', start)
                index = name[start:end]
                input_index = name[start:last_underscore]
                pattern = inputdata.get('input'+input_index)
                if mr != 'MR11' and mr != 'MR9':
                    command = ["./a.out", '-E', pattern, './targetFiles/file.test']
                elif mr == 'MR11':
                    command = ["./a.out", '-E', pattern, './targetFiles/MR11_' + index]
                else:
                    command = ["./a.out", '-E', pattern, './targetFiles/file.test']
            else:
                start = name.find('output_follow') + len('output_follow')
                end = name.find('_', start)
                index = name[start:end]
                input_index = name[start:]
                pattern = inputdata.get('input'+input_index)
                if mr != 'MR11' and mr != 'MR9':
                    command = ["./a.out", '-E', pattern, './targetFiles/file.test']
                elif mr == 'MR11':
                    command = ["./a.out", '-E', pattern, './targetFiles/MR11_' + index]
                else:
                    command = ["./a.out", '-E', pattern, './targetFiles/file.test_MR9_follow']

            try:
                # output = subprocess.check_output(command)
                timeout_seconds = 60  # 设置超时时间为60秒
                # 启动进程
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    # 执行命令并设置超时时间
                    output, error = process.communicate(timeout=timeout_seconds)
                    # 输出命令执行结果
                    # print(output.decode("utf-8"))
                except subprocess.TimeoutExpired:
                    # 如果命令超时，结束进程
                    process.kill()
                    # 输出超时信息
                    print("Command execution timeout!")
                    # label = 1
                    break
            except subprocess.CalledProcessError as e:
                output = e.output
                print(name+"执行失败，输出信息：", output.decode())
            else:
                # print("input{}执行成功，输出信息：\n".format(i), output.decode())
                pass

            k = 1  # 获取可执行行
            command = ["gcov", "grep.c"]
            try:
                output = subprocess.check_output(command)
            except subprocess.CalledProcessError as e:
                output = e.output
                print(name+"命令执行失败，错误信息：", output.decode())
            else:
                print(name+"命令执行成功，输出信息：\n", output.decode())
                # pass

            statevalue.append(name)
            statetitle.append("test cases")

            fp2 = open("grep.c.gcov")
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

            # for mu in range(1, num_mu+1):
            #     statetitle.append("Mutant{}".format(mu))
            statetitle.append("Oracle")
            if pq == 0:
                spamwriter1.writerow(statetitle)
                pq = 1
            # for mu in range(1, 12):
            #     output_oringinal = Output[0].get(name)
            #     output_mutant = Output[mu].get(name)
            #     if output_oringinal == output_mutant:
            #         statevalue.append(int('0'))
            #     else:
            #         statevalue.append(int('1'))
            output_oringinal = output1[name]
            output_mutant = output2[name]
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
            t += 1
            # break
        csvfile1.close()


#     with open('./coverage/statementResult1.csv', 'r') as file:
#         reader = csv.reader(file)
#         original_data = list(reader)
#     for i in range(3, 46):
#         with open('./coverage/statementResult{}.csv'.format(i), 'r') as file:
#             reader = csv.reader(file)
#             new_data = list(reader)
#
#         # 在新文件中创建一个临时文件，用于写入修改后的内容
#         with open('./coverage/temp.csv', 'w', newline='') as file:
#             writer = csv.writer(file)
#
#             # 将原始文件的首行插入到新文件的首行
#             writer.writerow(original_data[0])
#
#             # 将新文件的内容下移一行
#             writer.writerows(new_data)
#         # 删除原始文件
#         import os
#         os.remove('./coverage/statementResult{}.csv'.format(i))
#
#         # 将临时文件重命名为原始文件名
#         os.rename('./coverage/temp.csv', './coverage/statementResult{}.csv'.format(i))

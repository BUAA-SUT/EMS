import copy
import random
import numpy as np

# from openpyxl import load_workbook
random.seed(1)

Formula = ['Naish1', 'Naish2', 'Wong1', 'Russel&Rao', 'Binary', 'Jaccard', 'Anderberg', 'Sørensen-Dice', 'Dice',
           'Goodman', 'Tarantula', 'qe', 'CBI Inc.', 'Wong2', 'Hamann', 'Simple Matching', 'Sokal', 'Rogers&Tanimoto',
           'Hamming etc.', 'Euclid', 'Scott', 'Rogot1', 'Kulczynski2', 'Ochiai', 'M2', 'AMPLE2', 'Wong3',
           'Arithmetic Mean', 'Cohen', 'Fleiss']


def min_max_normalize(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized_data


def riskformula(index, t):  # 多个公式
    ev = index[0]
    es = index[1]
    nv = index[2]
    ns = index[3]
    ev_only = nv
    F = ev + nv
    P = es + ns
    if t == 0:
        if ev < F:
            formula = -1
        elif ev == F and F != 0:
            formula = ns
        else:
            formula = -1
    elif t == 1:
        formula = ev - es / (es + ns + 1)
    elif t == 2:
        formula = ev
    elif t == 3:
        formula = ev / (ev + es + nv + ns)
    elif t == 4:
        if ev < F:
            formula = 0
        elif ev == F and F != 0:
            formula = 1
        else:
            formula = 0
    elif t == 5:
        formula = ev / (ev + es + nv)
    elif t == 6:
        formula = ev / (ev + 2 * (nv + es))
    elif t == 7:
        formula = 2 * ev / (2 * ev + nv + es)
    elif t == 8:
        formula = 2 * ev / (ev + nv + es)
    elif t == 9:
        formula = (2 * ev - nv - es) / (2 * ev + nv + es)
    elif t == 10:
        formula = (ev / (ev + nv)) / (ev / (ev + nv) + es / (es + ns))
    elif t == 11:
        formula = ev / (ev + es)
    elif t == 12:
        formula = (ev / (ev + es)) - ((ev + nv) / (ev + nv + es + ns))
    elif t == 13:
        formula = ev - es
    elif t == 14:
        formula = (ev + ns - nv - es) / (ev + nv + es + ns)
    elif t == 15:
        formula = (ev + ns) / (ev + nv + es + ns)
    elif t == 16:
        formula = 2 * (ev + ns) / (2 * (ev + ns) + nv + es)
    elif t == 17:
        formula = (ev + ns) / (ev + ns + 2 * (nv + es))
    elif t == 18:
        formula = ev + ns
    elif t == 19:
        formula = np.sqrt(ev + ns)
    elif t == 20:
        formula = (4 * ev * ns - 4 * nv * es - (nv - es) ** 2) / ((2 * ev + nv + es) * (2 * ns + nv + es))
    elif t == 21:
        formula = 0.5 * (ev / (2 * ev + nv + es) + ns / (2 * ns + nv + es))
    elif t == 22:
        formula = 0.5 * (ev / (ev + nv) + ev / (ev + es))
    elif t == 23:
        formula = ev / ((ev + nv) * (ev + es)) ** 0.5
    elif t == 24:
        formula = ev / (ev + ns + 2 * (nv + es))
    elif t == 25:
        formula = ev / (ev + nv) - es / (es + ns)
    elif t == 26:
        if es <= 2:
            formula = ev - es
        elif 2 < es <= 10:
            formula = ev - 2 - 0.1 * (es - 2)
        else:
            formula = ev - 2.8 - 0.001 * (es - 10)
    elif t == 27:
        formula = (2 * ev * ns - 2 * nv * es) / ((ev + es) * (ns + nv) + (ev + nv) * (es + ns))
    elif t == 28:
        formula = (2 * ev * ns - 2 * nv * es) / ((ev + es) * (ns + es) + (ev + nv) * (nv + ns))
    else:
        formula = (4 * ev * ns - 4 * nv * es - (nv - es) ** 2) / (2 * ev + nv + es + 2 * ns + nv + es)

    return formula


def riskformula2(index, t, v, s):  # 多个公式
    ev = index[0]
    es = index[1]
    nv = index[2]
    ns = index[3]
    ev_only = nv
    F = v
    P = s
    if t == 0:
        if ev < F:
            formula = -1
        elif ev == F and F != 0:
            formula = ns
        else:
            formula = -1
    elif t == 1:
        formula = ev - es / (es + ns + 1)
    elif t == 2:
        formula = ev
    elif t == 3:
        formula = ev / (ev + es + nv + ns)
    elif t == 4:
        if ev < F:
            formula = 0
        elif ev == F and F != 0:
            formula = 1
        else:
            formula = 0
    elif t == 5:
        formula = ev / (ev + es + nv)
    elif t == 6:
        formula = ev / (ev + 2 * (nv + es))
    elif t == 7:
        formula = 2 * ev / (2 * ev + nv + es)
    elif t == 8:
        formula = 2 * ev / (ev + nv + es)
    elif t == 9:
        formula = (2 * ev - nv - es) / (2 * ev + nv + es)
    elif t == 10:
        formula = (ev / (ev + nv)) / (ev / (ev + nv) + es / (es + ns))
    elif t == 11:
        formula = ev / (ev + es)
    elif t == 12:
        formula = (ev / (ev + es)) - ((ev + nv) / (ev + nv + es + ns))
    elif t == 13:
        formula = ev - es
    elif t == 14:
        formula = (ev + ns - nv - es) / (ev + nv + es + ns)
    elif t == 15:
        formula = (ev + ns) / (ev + nv + es + ns)
    elif t == 16:
        formula = 2 * (ev + ns) / (2 * (ev + ns) + nv + es)
    elif t == 17:
        formula = (ev + ns) / (ev + ns + 2 * (nv + es))
    elif t == 18:
        formula = ev + ns
    elif t == 19:
        formula = np.sqrt(ev + ns)
    elif t == 20:
        formula = (4 * ev * ns - 4 * nv * es - (nv - es) ** 2) / ((2 * ev + nv + es) * (2 * ns + nv + es))
    elif t == 21:
        formula = 0.5 * (ev / (2 * ev + nv + es) + ns / (2 * ns + nv + es))
    elif t == 22:
        formula = 0.5 * (ev / (ev + nv) + ev / (ev + es))
    elif t == 23:
        formula = ev / ((ev + nv) * (ev + es)) ** 0.5
    elif t == 24:
        formula = ev / (ev + ns + 2 * (nv + es))
    elif t == 25:
        formula = ev / (ev + nv) - es / (es + ns)
    elif t == 26:
        if es <= 2:
            formula = ev - es
        elif 2 < es <= 10:
            formula = ev - 2 - 0.1 * (es - 2)
        else:
            formula = ev - 2.8 - 0.001 * (es - 10)
    elif t == 27:
        formula = (2 * ev * ns - 2 * nv * es) / ((ev + es) * (ns + nv) + (ev + nv) * (es + ns))
    elif t == 28:
        formula = (2 * ev * ns - 2 * nv * es) / ((ev + es) * (ns + es) + (ev + nv) * (nv + ns))
    else:
        formula = (4 * ev * ns - 4 * nv * es - (nv - es) ** 2) / (2 * ev + nv + es + 2 * ns + nv + es)

    return formula


def getSus(index, t):
    formula = 0
    try:
        formula = riskformula(index, t)
    except:
        if index[0] + index[1] == 0:  # e = 0
            formula = -1000
        elif index[0] + index[2] == 0:  # v = 0
            formula = -1000
        elif index[1] + index[3] == 0:  # s = 0
            formula = 1000
    return formula


def getSus2(index, t, v, s):
    formula = 0
    try:
        formula = riskformula2(index, t, v, s)
    except:
        if index[0] + index[1] == 0:  # e = 0
            formula = -1000
        elif index[0] + index[2] == 0:  # v = 0
            formula = -1000
        elif index[1] + index[3] == 0:  # s = 0
            formula = 1000
    return formula


def MSlice(MG, Executable, Exelines):
    metric = []
    Sus = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                exe.sort()
                union = list(set(Exelines[i][j]) & set(Exelines[i][j * len(MG[0][0]) + k + 1]))
                unique = [x for x in exe if x not in union]
                if len(unique) == 0 or len(union) == 0:
                    continue
                if MG[i][j][k] == 1:
                    v += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][0] += 1  # ev
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:  # or MG[i][j][k] == 3
                    s += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][1] += 1  # es
    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            # sus.append(round(getSus(metric[i], t), 4))
            sus.append(getSus(metric[i], t))
        Sus.append(sus)
    return Sus, metric


def MSlice_one(MG, Executable, Exelines, Flag, Result):
    metric = []
    Sus = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    fault = Executable[Flag.index(1)]
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                exe.sort()
                union = list(set(Exelines[i][j]) & set(Exelines[i][j * len(MG[0][0]) + k + 1]))
                unique = [x for x in exe if x not in union]
                if len(unique) == 0 or len(union) == 0:
                    continue
                if MG[i][j][k] == 1:
                    if Result[i][j] and Result[i][j * len(MG[0][0]) + k + 1] and fault in union:
                        continue
                    v += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][0] += 1  # ev
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:  # or MG[i][j][k] == 3
                    s += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][1] += 1  # es
    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            # sus.append(round(getSus(metric[i], t), 4))
            sus.append(getSus(metric[i], t))
        Sus.append(sus)
    return Sus, metric


def MSlice_all(MG, Executable, Exelines, Flag, Result):
    metric = []
    Sus = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    fault = Executable[Flag.index(1)]
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                exe.sort()
                union = list(set(Exelines[i][j]) & set(Exelines[i][j * len(MG[0][0]) + k + 1]))
                unique = [x for x in exe if x not in union]
                if len(unique) == 0 or len(union) == 0:
                    continue
                if MG[i][j][k] == 1:
                    if not (Result[i][j] and Result[i][j * len(MG[0][0]) + k + 1] and fault in union):
                        continue
                    v += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][0] += 1  # ev
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:  # or MG[i][j][k] == 3
                    s += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][1] += 1  # es
    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            # sus.append(round(getSus(metric[i], t), 4))
            sus.append(getSus(metric[i], t))
        Sus.append(sus)
    return Sus, metric


def MSlice2(MG, Executable, Exelines, Flag):
    Metric = []
    for _ in range(10):
        metric = []
        for i in range(len(Executable)):
            metric.append([0, 0, 0, 0])  # ev es nv ns
        Metric.append(metric)
    v = 0
    s = 0
    AllF = 0
    fault = Executable[Flag.index(1)]
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                union = list(set(Exelines[i][j]) & set(Exelines[i][j * len(MG[0][0]) + k + 1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if MG[i][j][k] == 1:
                    v += 1
                    if fault in Exelines[i][j] and fault in Exelines[i][j * len(MG[0][0]) + k + 1]:
                        AllF += 1
                    for d in union:
                        index = Executable.index(d)
                        Metric[0][index][0] += 1  # ev
                        Metric[1][index][0] += 1  # ev
                        Metric[2][index][0] += 1  # ev
                        Metric[3][index][0] += 1  # ev
                        Metric[4][index][0] += 1  # ev
                        Metric[5][index][0] += 0.9  # ev
                        Metric[6][index][0] += 0.8  # ev
                        Metric[7][index][0] += 0.7  # ev
                        Metric[8][index][0] += 0.6  # ev
                        Metric[9][index][0] += 0.5  # ev
                    for d in unique:
                        index = Executable.index(d)
                        Metric[0][index][0] += 0.9  # ev
                        Metric[1][index][0] += 0.8  # ev
                        Metric[2][index][0] += 0.7  # ev
                        Metric[3][index][0] += 0.6  # ev
                        Metric[4][index][0] += 0.5  # ev
                        Metric[5][index][0] += 1  # ev
                        Metric[6][index][0] += 1  # ev
                        Metric[7][index][0] += 1  # ev
                        Metric[8][index][0] += 1  # ev
                        Metric[9][index][0] += 1  # ev
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:
                    s += 1
                    for d in union:
                        index = Executable.index(d)
                        Metric[0][index][1] += 1  # es
                        Metric[1][index][1] += 1  # es
                        Metric[2][index][1] += 1  # es
                        Metric[3][index][1] += 1  # es
                        Metric[4][index][1] += 1  # es
                        Metric[5][index][1] += 0.9  # es
                        Metric[6][index][1] += 0.8  # es
                        Metric[7][index][1] += 0.7  # es
                        Metric[8][index][1] += 0.6  # es
                        Metric[9][index][1] += 0.5  # es
                    for d in unique:
                        index = Executable.index(d)
                        Metric[0][index][1] += 0.9  # es
                        Metric[1][index][1] += 0.8
                        Metric[2][index][1] += 0.7
                        Metric[3][index][1] += 0.6
                        Metric[4][index][1] += 0.5
                        Metric[5][index][1] += 1  # es
                        Metric[6][index][1] += 1
                        Metric[7][index][1] += 1
                        Metric[8][index][1] += 1
                        Metric[9][index][1] += 1
    for k in range(10):
        for i in range(len(Metric[k])):
            Metric[k][i][2] = v - Metric[k][i][0]
            Metric[k][i][3] = s - Metric[k][i][1]

    SUS = []
    for k in range(10):
        Sus = []
        for t in range(len(Formula)):
            sus = []
            for i in range(len(Metric[k])):
                sus.append(getSus(Metric[k][i], t))
            Sus.append(sus)
        SUS.append(Sus)
    if v == 0:
        AllF = 0
    else:
        AllF = round(AllF / v * 100, 2)
    return SUS, AllF, Metric


def MSlice3(MG, Executable, Exelines, Flag):
    """
    23.10.6
    将权重和是否经过拆分成两个矩阵，不是经过0.6个，是经过1个，权重变成0.6
    即nv, ns不变
    """
    Metric = []
    for _ in range(10):
        metric = []
        for i in range(len(Executable)):
            metric.append([0, 0, 0, 0])  # ev es nv ns
        Metric.append(metric)
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    AllF = 0
    fault = Executable[Flag.index(1)]
    Union = []
    Unique = []
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                union = list(set(Exelines[i][j]) & set(Exelines[i][j * len(MG[0][0]) + k + 1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if len(unique) == 0:
                    continue
                # if union in Union:
                #     pass
                # else:
                #     Union.append(union)
                # if unique in Unique:
                #     pass
                # else:
                #     Unique.append(unique)
                if MG[i][j][k] == 1:
                    v += 1
                    if fault in Exelines[i][j] and fault in Exelines[i][j * len(MG[0][0]) + k + 1]:
                        AllF += 1
                    for d in union:
                        index = Executable.index(d)
                        Metric[0][index][0] += 1  # ev
                        Metric[1][index][0] += 1  # ev
                        Metric[2][index][0] += 1  # ev
                        Metric[3][index][0] += 1  # ev
                        Metric[4][index][0] += 1  # ev
                        Metric[5][index][0] += 0.9  # ev
                        Metric[6][index][0] += 0.8  # ev
                        Metric[7][index][0] += 0.7  # ev
                        Metric[8][index][0] += 0.6  # ev
                        Metric[9][index][0] += 0.5  # ev
                        Metric2[index][0] += 1
                    for d in unique:
                        index = Executable.index(d)
                        Metric[0][index][0] += 0.9  # ev
                        Metric[1][index][0] += 0.8  # ev
                        Metric[2][index][0] += 0.7  # ev
                        Metric[3][index][0] += 0.6  # ev
                        Metric[4][index][0] += 0.5  # ev
                        Metric[5][index][0] += 1  # ev
                        Metric[6][index][0] += 1  # ev
                        Metric[7][index][0] += 1  # ev
                        Metric[8][index][0] += 1  # ev
                        Metric[9][index][0] += 1  # ev
                        Metric2[index][0] += 1
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:
                    s += 1
                    for d in union:
                        index = Executable.index(d)
                        Metric[0][index][1] += 1  # es
                        Metric[1][index][1] += 1  # es
                        Metric[2][index][1] += 1  # es
                        Metric[3][index][1] += 1  # es
                        Metric[4][index][1] += 1  # es
                        Metric[5][index][1] += 0.9  # es
                        Metric[6][index][1] += 0.8  # es
                        Metric[7][index][1] += 0.7  # es
                        Metric[8][index][1] += 0.6  # es
                        Metric[9][index][1] += 0.5  # es
                        Metric2[index][1] += 1
                    for d in unique:
                        index = Executable.index(d)
                        Metric[0][index][1] += 0.9  # es
                        Metric[1][index][1] += 0.8
                        Metric[2][index][1] += 0.7
                        Metric[3][index][1] += 0.6
                        Metric[4][index][1] += 0.5
                        Metric[5][index][1] += 1  # es
                        Metric[6][index][1] += 1
                        Metric[7][index][1] += 1
                        Metric[8][index][1] += 1
                        Metric[9][index][1] += 1
                        Metric2[index][1] += 1
    for k in range(10):
        for i in range(len(Metric[k])):
            Metric[k][i][2] = v - Metric2[i][0]
            Metric[k][i][3] = s - Metric2[i][1]

    SUS = []
    for k in range(10):
        Sus = []
        for t in range(len(Formula)):
            sus = []
            for i in range(len(Metric[k])):
                sus.append(getSus2(Metric[k][i], t, v, s))
            Sus.append(sus)
        SUS.append(Sus)
    if v == 0:
        AllF = 0
    else:
        AllF = round(AllF / v * 100, 2)
    return SUS, AllF, Metric


def MSlice4(MG, Executable, Exelines, Flag, Result):
    """
    23.12.14
    将权重和是否经过拆分成两个矩阵，不是经过0.6个，是经过1个，权重变成0.6
    即nv, ns不变
    调整权重步长
    """
    Metric = []
    for _ in range(50):
        metric = []
        for i in range(len(Executable)):
            metric.append([0, 0, 0, 0])  # ev es nv ns
        Metric.append(metric)
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    AllF = 0
    j1 = 0
    c1 = 0
    b1 = 0
    j2 = 0
    c2 = 0
    b2 = 0
    j3 = 0
    c3 = 0
    b3 = 0
    fault = Executable[Flag.index(1)]
    jiao1 = 0
    cha1 = 0
    jiao2 = 0
    cha2 = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                union = list(set(Exelines[i][j]) & set(Exelines[i][j * len(MG[0][0]) + k + 1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if len(unique) == 0 or len(union) == 0:
                    continue
                j1 += len(union)
                c1 += len(unique)
                b1 += len(exe)
                if MG[i][j][k] == 1:
                    if fault in union:
                        jiao1 += 1
                    if fault in unique:
                        cha1 += 1
                    j2 += len(union)
                    c2 += len(unique)
                    b2 += len(exe)
                    v += 1
                    if Result[i][j] and Result[i][j * len(MG[0][0]) + k + 1]:
                        AllF += 1
                    for d in union:
                        index = Executable.index(d)
                        for x in range(25):
                            Metric[x][index][0] += 1  # ev
                        t = 1
                        for y in range(25, 50):
                            Metric[y][index][0] += 1-0.02*t  # ev
                            Metric[y][index][0] = round(Metric[y][index][0], 2)
                            t += 1
                        Metric2[index][0] += 1
                    for d in unique:
                        index = Executable.index(d)
                        t = 1
                        for x in range(25):
                            Metric[x][index][0] += 1-0.02*t  # ev
                            Metric[x][index][0] = round(Metric[x][index][0], 2)
                            t += 1
                        for y in range(25, 50):
                            Metric[y][index][0] += 1  # ev
                        Metric2[index][0] += 1
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:  # or MG[i][j][k] == 3
                    if fault in union:
                        jiao2 += 1
                    if fault in unique:
                        cha2 += 1
                    j3 += len(union)
                    c3 += len(unique)
                    b3 += len(exe)
                    s += 1
                    for d in union:
                        index = Executable.index(d)
                        for x in range(25):
                            Metric[x][index][1] += 1  # es
                        t = 1
                        for y in range(25, 50):
                            Metric[y][index][1] += 1-0.02*t  # es
                            Metric[y][index][1] = round(Metric[y][index][1], 2)
                            t += 1
                        Metric2[index][1] += 1
                    for d in unique:
                        index = Executable.index(d)
                        t = 1
                        for x in range(25):
                            Metric[x][index][1] += 1-0.02*t  # es
                            Metric[x][index][1] = round(Metric[x][index][1], 2)
                            t += 1
                        for y in range(25, 50):
                            Metric[y][index][1] += 1  # es
                        Metric2[index][1] += 1
    for k in range(50):
        for i in range(len(Metric[k])):
            Metric[k][i][2] = v - Metric2[i][0]
            Metric[k][i][3] = s - Metric2[i][1]
    # print("vmg交集{}".format(jiao1))
    # print("vmg差集{}".format(cha1))
    # print("smg交集{}".format(jiao2))
    # print("smg差集{}".format(cha2))
    a = 0
    for i in range(len(Result)):
        for j in range(len(Result[i])):
            if Result[i][j] == 0 and fault in Exelines[i][j]:
                a += 1
    EnF = round(a / (len(Result) * len(Result[0])) * 100, 2)
    SUS = []
    for k in range(50):
        Sus = []
        for t in range(len(Formula)):
            sus = []
            for i in range(len(Metric[k])):
                sus.append(round(getSus2(Metric[k][i], t, v, s), 4))
            Sus.append(sus)
        SUS.append(Sus)
    if b1 == 0:
        j1p = 0
        c1p = 0
    else:
        j1p = round(j1 / b1 * 100, 2)
        c1p = round(c1 / b1 * 100, 2)
    if v == 0:
        AllF = 0
        j2p = 0
        c2p = 0
    else:
        AllF = round(AllF / v * 100, 2)
        j2p = round(j2 / b2 * 100, 2)
        c2p = round(c2 / b2 * 100, 2)
    if s == 0:
        j3p = 0
        c3p = 0
    else:
        j3p = round(j3 / b3 * 100, 2)
        c3p = round(c3 / b3 * 100, 2)
    Para = [j1p, c1p, j2p, c2p, j3p, c3p, EnF, AllF]
    return SUS, Para, Metric


def MSlice4_one(MG, Executable, Exelines, Flag, Result):
    """
    23.12.14
    将权重和是否经过拆分成两个矩阵，不是经过0.6个，是经过1个，权重变成0.6
    即nv, ns不变
    调整权重步长
    """
    Metric = []
    for _ in range(50):
        metric = []
        for i in range(len(Executable)):
            metric.append([0, 0, 0, 0])  # ev es nv ns
        Metric.append(metric)
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    AllF = 0
    j1 = 0
    c1 = 0
    b1 = 0
    j2 = 0
    c2 = 0
    b2 = 0
    j3 = 0
    c3 = 0
    b3 = 0
    fault = Executable[Flag.index(1)]
    jiao1 = 0
    cha1 = 0
    jiao2 = 0
    cha2 = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                union = list(set(Exelines[i][j]) & set(Exelines[i][j * len(MG[0][0]) + k + 1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if len(unique) == 0 or len(union) == 0:
                    continue
                j1 += len(union)
                c1 += len(unique)
                b1 += len(exe)
                if MG[i][j][k] == 1:
                    if fault in union:
                        jiao1 += 1
                    if fault in unique:
                        cha1 += 1
                    j2 += len(union)
                    c2 += len(unique)
                    b2 += len(exe)
                    if Result[i][j] and Result[i][j * len(MG[0][0]) + k + 1] and fault in union:
                        AllF += 1
                        continue
                    v += 1
                    for d in union:
                        index = Executable.index(d)
                        for x in range(25):
                            Metric[x][index][0] += 1  # ev
                        t = 1
                        for y in range(25, 50):
                            Metric[y][index][0] += 1-0.02*t  # ev
                            Metric[y][index][0] = round(Metric[y][index][0], 2)
                            t += 1
                        Metric2[index][0] += 1
                    for d in unique:
                        index = Executable.index(d)
                        t = 1
                        for x in range(25):
                            Metric[x][index][0] += 1-0.02*t  # ev
                            Metric[x][index][0] = round(Metric[x][index][0], 2)
                            t += 1
                        for y in range(25, 50):
                            Metric[y][index][0] += 1  # ev
                        Metric2[index][0] += 1
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:  # or MG[i][j][k] == 3
                    if fault in union:
                        jiao2 += 1
                    if fault in unique:
                        cha2 += 1
                    j3 += len(union)
                    c3 += len(unique)
                    b3 += len(exe)
                    s += 1
                    for d in union:
                        index = Executable.index(d)
                        for x in range(25):
                            Metric[x][index][1] += 1  # ev
                        t = 1
                        for y in range(25, 50):
                            Metric[y][index][1] += 1-0.02*t  # ev
                            Metric[y][index][1] = round(Metric[y][index][1], 2)
                            t += 1
                        Metric2[index][1] += 1
                    for d in unique:
                        index = Executable.index(d)
                        t = 1
                        for x in range(25):
                            Metric[x][index][1] += 1-0.02*t  # ev
                            Metric[x][index][1] = round(Metric[x][index][1], 2)
                            t += 1
                        for y in range(25, 50):
                            Metric[y][index][1] += 1  # ev
                        Metric2[index][1] += 1
    for k in range(50):
        for i in range(len(Metric[k])):
            Metric[k][i][2] = v - Metric2[i][0]
            Metric[k][i][3] = s - Metric2[i][1]
    # print("vmg交集{}".format(jiao1))
    # print("vmg差集{}".format(cha1))
    # print("smg交集{}".format(jiao2))
    # print("smg差集{}".format(cha2))
    a = 0
    for i in range(len(Result)):
        for j in range(len(Result[i])):
            if Result[i][j] == 0 and fault in Exelines[i][j]:
                a += 1
    EnF = round(a / (len(Result) * len(Result[0])) * 100, 2)
    SUS = []
    for k in range(50):
        Sus = []
        for t in range(len(Formula)):
            sus = []
            for i in range(len(Metric[k])):
                sus.append(round(getSus2(Metric[k][i], t, v, s), 4))
            Sus.append(sus)
        SUS.append(Sus)
    if b1 == 0:
        j1p = 0
        c1p = 0
    else:
        j1p = round(j1 / b1 * 100, 2)
        c1p = round(c1 / b1 * 100, 2)
    if v == 0:
        AllF = 0
        j2p = 0
        c2p = 0
    else:
        AllF = round(AllF / v * 100, 2)
        j2p = round(j2 / b2 * 100, 2)
        c2p = round(c2 / b2 * 100, 2)
    if s == 0:
        j3p = 0
        c3p = 0
    else:
        j3p = round(j3 / b3 * 100, 2)
        c3p = round(c3 / b3 * 100, 2)
    Para = [j1p, c1p, j2p, c2p, j3p, c3p, EnF, AllF]
    return SUS, Para, Metric


def MSlice4_all(MG, Executable, Exelines, Flag, Result):
    """
    23.12.14
    将权重和是否经过拆分成两个矩阵，不是经过0.6个，是经过1个，权重变成0.6
    即nv, ns不变
    调整权重步长
    """
    Metric = []
    for _ in range(50):
        metric = []
        for i in range(len(Executable)):
            metric.append([0, 0, 0, 0])  # ev es nv ns
        Metric.append(metric)
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    AllF = 0
    j1 = 0
    c1 = 0
    b1 = 0
    j2 = 0
    c2 = 0
    b2 = 0
    j3 = 0
    c3 = 0
    b3 = 0
    fault = Executable[Flag.index(1)]
    jiao1 = 0
    cha1 = 0
    jiao2 = 0
    cha2 = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                union = list(set(Exelines[i][j]) & set(Exelines[i][j * len(MG[0][0]) + k + 1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if len(unique) == 0 or len(union) == 0:
                    continue
                j1 += len(union)
                c1 += len(unique)
                b1 += len(exe)
                if MG[i][j][k] == 1:
                    if fault in union:
                        jiao1 += 1
                    if fault in unique:
                        cha1 += 1
                    j2 += len(union)
                    c2 += len(unique)
                    b2 += len(exe)
                    if Result[i][j] and Result[i][j * len(MG[0][0]) + k + 1] and fault in union:
                        AllF += 1
                    if not (Result[i][j] and Result[i][j * len(MG[0][0]) + k + 1] and fault in union):
                        continue
                    v += 1
                    for d in union:
                        index = Executable.index(d)
                        for x in range(25):
                            Metric[x][index][0] += 1  # ev
                        t = 1
                        for y in range(25, 50):
                            Metric[y][index][0] += 1-0.02*t  # ev
                            Metric[y][index][0] = round(Metric[y][index][0], 2)
                            t += 1
                        Metric2[index][0] += 1
                    for d in unique:
                        index = Executable.index(d)
                        t = 1
                        for x in range(25):
                            Metric[x][index][0] += 1-0.02*t  # ev
                            Metric[x][index][0] = round(Metric[x][index][0], 2)
                            t += 1
                        for y in range(25, 50):
                            Metric[y][index][0] += 1  # ev
                        Metric2[index][0] += 1
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:  # or MG[i][j][k] == 3
                    if fault in union:
                        jiao2 += 1
                    if fault in unique:
                        cha2 += 1
                    j3 += len(union)
                    c3 += len(unique)
                    b3 += len(exe)
                    s += 1
                    for d in union:
                        index = Executable.index(d)
                        for x in range(25):
                            Metric[x][index][1] += 1  # ev
                        t = 1
                        for y in range(25, 50):
                            Metric[y][index][1] += 1-0.02*t  # ev
                            Metric[y][index][1] = round(Metric[y][index][1], 2)
                            t += 1
                        Metric2[index][1] += 1
                    for d in unique:
                        index = Executable.index(d)
                        t = 1
                        for x in range(25):
                            Metric[x][index][1] += 1-0.02*t  # ev
                            Metric[x][index][1] = round(Metric[x][index][1], 2)
                            t += 1
                        for y in range(25, 50):
                            Metric[y][index][1] += 1  # ev
                        Metric2[index][1] += 1
    for k in range(50):
        for i in range(len(Metric[k])):
            Metric[k][i][2] = v - Metric2[i][0]
            Metric[k][i][3] = s - Metric2[i][1]
    # print("vmg交集{}".format(jiao1))
    # print("vmg差集{}".format(cha1))
    # print("smg交集{}".format(jiao2))
    # print("smg差集{}".format(cha2))
    a = 0
    for i in range(len(Result)):
        for j in range(len(Result[i])):
            if Result[i][j] == 0 and fault in Exelines[i][j]:
                a += 1
    EnF = round(a / (len(Result) * len(Result[0])) * 100, 2)
    SUS = []
    for k in range(50):
        Sus = []
        for t in range(len(Formula)):
            sus = []
            for i in range(len(Metric[k])):
                sus.append(round(getSus2(Metric[k][i], t, v, s), 4))
            Sus.append(sus)
        SUS.append(Sus)
    if b1 == 0:
        j1p = 0
        c1p = 0
    else:
        j1p = round(j1 / b1 * 100, 2)
        c1p = round(c1 / b1 * 100, 2)
    if v == 0:
        AllF = 0
        j2p = 0
        c2p = 0
    else:
        AllF = round(AllF / v * 100, 2)
        j2p = round(j2 / b2 * 100, 2)
        c2p = round(c2 / b2 * 100, 2)
    if s == 0:
        j3p = 0
        c3p = 0
    else:
        j3p = round(j3 / b3 * 100, 2)
        c3p = round(c3 / b3 * 100, 2)
    Para = [j1p, c1p, j2p, c2p, j3p, c3p, EnF, AllF]
    return SUS, Para, Metric


def MSlice_grep(MG, Executable, Exelines):
    metric = []
    Sus = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                union = list(set(Exelines[i][j][k][0]) & set(Exelines[i][j][k][1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if len(unique) == 0 or len(union) == 0:
                    continue
                if MG[i][j][k] == 1:
                    v += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][0] += 1  # ev
                    # 将for循环转换成列表推导式
                    # b_indices = {value: index for index, value in enumerate(Executable)}
                    # a_indices = [b_indices[value] for value in exe if value in b_indices]
                    # metric = [value if index not in a_indices else [value[0]+1, value[1], value[2], value[3]]
                    #           for index, value in enumerate(metric)]
                elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                    s += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][1] += 1  # es
                    # 将for循环转换成列表推导式，效率还不如上面
                    # b_indices = {value: index for index, value in enumerate(Executable)}
                    # a_indices = [b_indices[value] for value in exe if value in b_indices]
                    # metric = [value if index not in a_indices else [value[0], value[1]+1, value[2], value[3]]
                    #           for index, value in enumerate(metric)]

    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            # sus.append(round(getSus(metric[i], t), 4))
            sus.append(getSus(metric[i], t))
        Sus.append(sus)
    return Sus, metric


def MSlice_grep_one(MG, Executable, Exelines, Flag, Result):
    metric = []
    Sus = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    fault = Executable[Flag.index(1)]
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                union = list(set(Exelines[i][j][k][0]) & set(Exelines[i][j][k][1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if len(unique) == 0 or len(union) == 0:
                    continue
                if MG[i][j][k] == 1:
                    if Result[i][j][k][0] and Result[i][j][k][1] and fault in union:
                        continue
                    v += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][0] += 1  # ev
                    # 将for循环转换成列表推导式
                    # b_indices = {value: index for index, value in enumerate(Executable)}
                    # a_indices = [b_indices[value] for value in exe if value in b_indices]
                    # metric = [value if index not in a_indices else [value[0]+1, value[1], value[2], value[3]]
                    #           for index, value in enumerate(metric)]
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:  # or MG[i][j][k] == 3
                    s += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][1] += 1  # es
                    # 将for循环转换成列表推导式，效率还不如上面
                    # b_indices = {value: index for index, value in enumerate(Executable)}
                    # a_indices = [b_indices[value] for value in exe if value in b_indices]
                    # metric = [value if index not in a_indices else [value[0], value[1]+1, value[2], value[3]]
                    #           for index, value in enumerate(metric)]

    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            # sus.append(round(getSus(metric[i], t), 4))
            sus.append(getSus(metric[i], t))
        Sus.append(sus)
    return Sus, metric


def MSlice_grep_all(MG, Executable, Exelines, Flag, Result):
    metric = []
    Sus = []
    for i in range(len(Executable)):
        metric.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    fault = Executable[Flag.index(1)]
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                union = list(set(Exelines[i][j][k][0]) & set(Exelines[i][j][k][1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if len(unique) == 0 or len(union) == 0:
                    continue
                if MG[i][j][k] == 1:
                    if not (Result[i][j][k][0] and Result[i][j][k][1] and fault in union):
                        continue
                    v += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][0] += 1  # ev
                    # 将for循环转换成列表推导式
                    # b_indices = {value: index for index, value in enumerate(Executable)}
                    # a_indices = [b_indices[value] for value in exe if value in b_indices]
                    # metric = [value if index not in a_indices else [value[0]+1, value[1], value[2], value[3]]
                    #           for index, value in enumerate(metric)]
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:  # or MG[i][j][k] == 3
                    s += 1
                    for d in exe:
                        index = Executable.index(d)
                        metric[index][1] += 1  # es
                    # 将for循环转换成列表推导式，效率还不如上面
                    # b_indices = {value: index for index, value in enumerate(Executable)}
                    # a_indices = [b_indices[value] for value in exe if value in b_indices]
                    # metric = [value if index not in a_indices else [value[0], value[1]+1, value[2], value[3]]
                    #           for index, value in enumerate(metric)]

    for i in range(len(metric)):
        metric[i][2] = v - metric[i][0]
        metric[i][3] = s - metric[i][1]
    for t in range(len(Formula)):
        sus = []
        for i in range(len(metric)):
            # sus.append(round(getSus(metric[i], t), 4))
            sus.append(getSus(metric[i], t))
        Sus.append(sus)
    return Sus, metric


def MSlice_grep2(MG, Executable, Exelines, Flag):
    Metric = []
    for _ in range(10):
        metric = []
        for i in range(len(Executable)):
            metric.append([0, 0, 0, 0])  # ev es nv ns
        Metric.append(metric)
    v = 0
    s = 0
    AllF = 0
    fault = Executable[Flag.index(1)]
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                union = list(set(Exelines[i][j][k][0]) & set(Exelines[i][j][k][1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if MG[i][j][k] == 1:
                    v += 1
                    if fault in Exelines[i][j][k][0] and fault in Exelines[i][j][k][1]:
                        AllF += 1
                    for d in union:
                        index = Executable.index(d)
                        Metric[0][index][0] += 1  # ev
                        Metric[1][index][0] += 1  # ev
                        Metric[2][index][0] += 1  # ev
                        Metric[3][index][0] += 1  # ev
                        Metric[4][index][0] += 1  # ev
                        Metric[5][index][0] += 0.9  # ev
                        Metric[6][index][0] += 0.8  # ev
                        Metric[7][index][0] += 0.7  # ev
                        Metric[8][index][0] += 0.6  # ev
                        Metric[9][index][0] += 0.5  # ev
                    for d in unique:
                        index = Executable.index(d)
                        Metric[0][index][0] += 0.9  # ev
                        Metric[1][index][0] += 0.8  # ev
                        Metric[2][index][0] += 0.7  # ev
                        Metric[3][index][0] += 0.6  # ev
                        Metric[4][index][0] += 0.5  # ev
                        Metric[5][index][0] += 1  # ev
                        Metric[6][index][0] += 1  # ev
                        Metric[7][index][0] += 1  # ev
                        Metric[8][index][0] += 1  # ev
                        Metric[9][index][0] += 1  # ev
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:
                    s += 1
                    for d in union:
                        index = Executable.index(d)
                        Metric[0][index][1] += 1  # es
                        Metric[1][index][1] += 1  # es
                        Metric[2][index][1] += 1  # es
                        Metric[3][index][1] += 1  # es
                        Metric[4][index][1] += 1  # es
                        Metric[5][index][1] += 0.9  # es
                        Metric[6][index][1] += 0.8  # es
                        Metric[7][index][1] += 0.7  # es
                        Metric[8][index][1] += 0.6  # es
                        Metric[9][index][1] += 0.5  # es
                    for d in unique:
                        index = Executable.index(d)
                        Metric[0][index][1] += 0.9  # es
                        Metric[1][index][1] += 0.8
                        Metric[2][index][1] += 0.7
                        Metric[3][index][1] += 0.6
                        Metric[4][index][1] += 0.5
                        Metric[5][index][1] += 1  # es
                        Metric[6][index][1] += 1
                        Metric[7][index][1] += 1
                        Metric[8][index][1] += 1
                        Metric[9][index][1] += 1
    for k in range(10):
        for i in range(len(Metric[k])):
            Metric[k][i][2] = v - Metric[k][i][0]
            Metric[k][i][3] = s - Metric[k][i][1]
    SUS = []
    for k in range(10):
        Sus = []
        for t in range(len(Formula)):
            sus = []
            for i in range(len(Metric[k])):
                sus.append(getSus(Metric[k][i], t))
            Sus.append(sus)
        SUS.append(Sus)
    if v == 0:
        AllF = 0
    else:
        AllF = round(AllF / v * 100, 2)
    return SUS, AllF, Metric


def MSlice_grep3(MG, Executable, Exelines, Flag):
    '''
    23.10.6
    将权重和是否经过拆分成两个矩阵，不是经过0.6个，是经过1个，权重变成0.6
    即nv, ns不变
    '''
    Metric = []
    for _ in range(10):
        metric = []
        for i in range(len(Executable)):
            metric.append([0, 0, 0, 0])  # ev es nv ns
        Metric.append(metric)
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    AllF = 0
    fault = Executable[Flag.index(1)]
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                union = list(set(Exelines[i][j][k][0]) & set(Exelines[i][j][k][1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if MG[i][j][k] == 1:
                    v += 1
                    if fault in Exelines[i][j][k][0] and fault in Exelines[i][j][k][1]:
                        AllF += 1
                    for d in union:
                        index = Executable.index(d)
                        Metric[0][index][0] += 1  # ev
                        Metric[1][index][0] += 1  # ev
                        Metric[2][index][0] += 1  # ev
                        Metric[3][index][0] += 1  # ev
                        Metric[4][index][0] += 1  # ev
                        Metric[5][index][0] += 0.9  # ev
                        Metric[6][index][0] += 0.8  # ev
                        Metric[7][index][0] += 0.7  # ev
                        Metric[8][index][0] += 0.6  # ev
                        Metric[9][index][0] += 0.5  # ev
                        Metric2[index][0] += 1
                    for d in unique:
                        index = Executable.index(d)
                        Metric[0][index][0] += 0.9  # ev
                        Metric[1][index][0] += 0.8  # ev
                        Metric[2][index][0] += 0.7  # ev
                        Metric[3][index][0] += 0.6  # ev
                        Metric[4][index][0] += 0.5  # ev
                        Metric[5][index][0] += 1  # ev
                        Metric[6][index][0] += 1  # ev
                        Metric[7][index][0] += 1  # ev
                        Metric[8][index][0] += 1  # ev
                        Metric[9][index][0] += 1  # ev
                        Metric2[index][0] += 1
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:
                    s += 1
                    for d in union:
                        index = Executable.index(d)
                        Metric[0][index][1] += 1  # es
                        Metric[1][index][1] += 1  # es
                        Metric[2][index][1] += 1  # es
                        Metric[3][index][1] += 1  # es
                        Metric[4][index][1] += 1  # es
                        Metric[5][index][1] += 0.9  # es
                        Metric[6][index][1] += 0.8  # es
                        Metric[7][index][1] += 0.7  # es
                        Metric[8][index][1] += 0.6  # es
                        Metric[9][index][1] += 0.5  # es
                        Metric2[index][1] += 1
                    for d in unique:
                        index = Executable.index(d)
                        Metric[0][index][1] += 0.9  # es
                        Metric[1][index][1] += 0.8
                        Metric[2][index][1] += 0.7
                        Metric[3][index][1] += 0.6
                        Metric[4][index][1] += 0.5
                        Metric[5][index][1] += 1  # es
                        Metric[6][index][1] += 1
                        Metric[7][index][1] += 1
                        Metric[8][index][1] += 1
                        Metric[9][index][1] += 1
                        Metric2[index][1] += 1
    for k in range(10):
        for i in range(len(Metric[k])):
            Metric[k][i][2] = v - Metric2[i][0]
            Metric[k][i][3] = s - Metric2[i][1]
    SUS = []
    for k in range(10):
        Sus = []
        for t in range(len(Formula)):
            sus = []
            for i in range(len(Metric[k])):
                sus.append(getSus2(Metric[k][i], t, v, s))
            Sus.append(sus)
        SUS.append(Sus)
    if v == 0:
        AllF = 0
    else:
        AllF = round(AllF / v * 100, 2)
    return SUS, AllF, Metric


def MSlice_grep4(MG, Executable, Exelines, Flag, Result):
    """
    23.10.6
    将权重和是否经过拆分成两个矩阵，不是经过0.6个，是经过1个，权重变成0.6
    即nv, ns不变
    调整权重步长
    """
    Metric = []
    for _ in range(50):
        metric = []
        for i in range(len(Executable)):
            metric.append([0, 0, 0, 0])  # ev es nv ns
        Metric.append(metric)
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    AllF = 0
    fault = Executable[Flag.index(1)]
    j1 = 0
    c1 = 0
    b1 = 0
    j2 = 0
    c2 = 0
    b2 = 0
    j3 = 0
    c3 = 0
    b3 = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                union = list(set(Exelines[i][j][k][0]) & set(Exelines[i][j][k][1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if len(unique) == 0 or len(union) == 0:
                    continue
                j1 += len(union)
                c1 += len(unique)
                b1 += len(exe)
                if MG[i][j][k] == 1:
                    j2 += len(union)
                    c2 += len(unique)
                    b2 += len(exe)
                    v += 1
                    if Result[i][j][k][0] and Result[i][j][k][1]:
                        AllF += 1
                    for d in union:
                        index = Executable.index(d)
                        for x in range(25):
                            Metric[x][index][0] += 1  # ev
                        t = 1
                        for y in range(25, 50):
                            Metric[y][index][0] += 1-0.02*t  # ev
                            Metric[y][index][0] = round(Metric[y][index][0], 2)
                            t += 1
                        Metric2[index][0] += 1
                    for d in unique:
                        index = Executable.index(d)
                        t = 1
                        for x in range(25):
                            Metric[x][index][0] += 1-0.02*t  # ev
                            Metric[x][index][0] = round(Metric[x][index][0], 2)
                            t += 1
                        for y in range(25, 50):
                            Metric[y][index][0] += 1  # ev
                        Metric2[index][0] += 1
                elif MG[i][j][k] == 0:  # or MG[i][j][k] == 3
                    j3 += len(union)
                    c3 += len(unique)
                    b3 += len(exe)
                    s += 1
                    for d in union:
                        index = Executable.index(d)
                        for x in range(25):
                            Metric[x][index][1] += 1  # ev
                        t = 1
                        for y in range(25, 50):
                            Metric[y][index][1] += 1-0.02*t  # ev
                            Metric[y][index][1] = round(Metric[y][index][1], 2)
                            t += 1
                        Metric2[index][1] += 1
                    for d in unique:
                        index = Executable.index(d)
                        t = 1
                        for x in range(25):
                            Metric[x][index][1] += 1-0.02*t  # ev
                            Metric[x][index][1] = round(Metric[x][index][1], 2)
                            t += 1
                        for y in range(25, 50):
                            Metric[y][index][1] += 1  # ev
                        Metric2[index][1] += 1

    for k in range(50):
        for i in range(len(Metric[k])):
            Metric[k][i][2] = v - Metric2[i][0]
            Metric[k][i][3] = s - Metric2[i][1]
    a = 0
    b = 0
    for i in range(len(Result)):
        for j in range(len(Result[i])):
            for m in range(len(Result[i][j])):
                for n in range(len(Result[i][j][m])):
                    b += 1
                    if Result[i][j][m][n] == 0 and fault in Exelines[i][j][m][n]:
                        a += 1
    EnF = round(a / b * 100, 2)

    SUS = []
    for k in range(50):
        Sus = []
        for t in range(len(Formula)):
            sus = []
            for i in range(len(Metric[k])):
                sus.append(getSus2(Metric[k][i], t, v, s))
            Sus.append(sus)
        SUS.append(Sus)
    if b1 == 0:
        j1p = 0
        c1p = 0
    else:
        j1p = round(j1 / b1 * 100, 2)
        c1p = round(c1 / b1 * 100, 2)
    if v == 0:
        AllF = 0
        j2p = 0
        c2p = 0
    else:
        AllF = round(AllF / v * 100, 2)
        j2p = round(j2 / b2 * 100, 2)
        c2p = round(c2 / b2 * 100, 2)
    if s == 0:
        j3p = 0
        c3p = 0
    else:
        j3p = round(j3 / b3 * 100, 2)
        c3p = round(c3 / b3 * 100, 2)
    Para = [j1p, c1p, j2p, c2p, j3p, c3p, EnF, AllF]
    return SUS, Para, Metric


def MSlice_grep4_one(MG, Executable, Exelines, Flag, Result):
    """
    23.10.6
    将权重和是否经过拆分成两个矩阵，不是经过0.6个，是经过1个，权重变成0.6
    即nv, ns不变
    调整权重步长
    """
    Metric = []
    for _ in range(50):
        metric = []
        for i in range(len(Executable)):
            metric.append([0, 0, 0, 0])  # ev es nv ns
        Metric.append(metric)
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    AllF = 0
    fault = Executable[Flag.index(1)]
    j1 = 0
    c1 = 0
    b1 = 0
    j2 = 0
    c2 = 0
    b2 = 0
    j3 = 0
    c3 = 0
    b3 = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                union = list(set(Exelines[i][j][k][0]) & set(Exelines[i][j][k][1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if len(unique) == 0 or len(union) == 0:
                    continue
                j1 += len(union)
                c1 += len(unique)
                b1 += len(exe)
                if MG[i][j][k] == 1:
                    if Result[i][j][k][0] and Result[i][j][k][1] and fault in union:
                        continue
                    j2 += len(union)
                    c2 += len(unique)
                    b2 += len(exe)
                    v += 1
                    if Result[i][j][k][0] and Result[i][j][k][1]:
                        AllF += 1
                    for d in union:
                        index = Executable.index(d)
                        for x in range(25):
                            Metric[x][index][0] += 1  # ev
                        t = 1
                        for y in range(25, 50):
                            Metric[y][index][0] += 1-0.02*t  # ev
                            Metric[y][index][0] = round(Metric[y][index][0], 2)
                            t += 1
                        Metric2[index][0] += 1
                    for d in unique:
                        index = Executable.index(d)
                        t = 1
                        for x in range(25):
                            Metric[x][index][0] += 1-0.02*t  # ev
                            Metric[x][index][0] = round(Metric[x][index][0], 2)
                            t += 1
                        for y in range(25, 50):
                            Metric[y][index][0] += 1  # ev
                        Metric2[index][0] += 1
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:  # or MG[i][j][k] == 3
                    j3 += len(union)
                    c3 += len(unique)
                    b3 += len(exe)
                    s += 1
                    for d in union:
                        index = Executable.index(d)
                        for x in range(25):
                            Metric[x][index][1] += 1  # ev
                        t = 1
                        for y in range(25, 50):
                            Metric[y][index][1] += 1-0.02*t  # ev
                            Metric[y][index][1] = round(Metric[y][index][1], 2)
                            t += 1
                        Metric2[index][1] += 1
                    for d in unique:
                        index = Executable.index(d)
                        t = 1
                        for x in range(25):
                            Metric[x][index][1] += 1-0.02*t  # ev
                            Metric[x][index][1] = round(Metric[x][index][1], 2)
                            t += 1
                        for y in range(25, 50):
                            Metric[y][index][1] += 1  # ev
                        Metric2[index][1] += 1

    for k in range(50):
        for i in range(len(Metric[k])):
            Metric[k][i][2] = v - Metric2[i][0]
            Metric[k][i][3] = s - Metric2[i][1]
    a = 0
    b = 0
    for i in range(len(Result)):
        for j in range(len(Result[i])):
            for m in range(len(Result[i][j])):
                for n in range(len(Result[i][j][m])):
                    b += 1
                    if Result[i][j][m][n] == 0 and fault in Exelines[i][j][m][n]:
                        a += 1
    EnF = round(a / b * 100, 2)

    SUS = []
    for k in range(50):
        Sus = []
        for t in range(len(Formula)):
            sus = []
            for i in range(len(Metric[k])):
                sus.append(getSus2(Metric[k][i], t, v, s))
            Sus.append(sus)
        SUS.append(Sus)
    if b1 == 0:
        j1p = 0
        c1p = 0
    else:
        j1p = round(j1 / b1 * 100, 2)
        c1p = round(c1 / b1 * 100, 2)
    if v == 0:
        AllF = 0
        j2p = 0
        c2p = 0
    else:
        AllF = round(AllF / v * 100, 2)
        j2p = round(j2 / b2 * 100, 2)
        c2p = round(c2 / b2 * 100, 2)
    if s == 0:
        j3p = 0
        c3p = 0
    else:
        j3p = round(j3 / b3 * 100, 2)
        c3p = round(c3 / b3 * 100, 2)
    Para = [j1p, c1p, j2p, c2p, j3p, c3p, EnF, AllF]
    return SUS, Para, Metric


def MSlice_grep4_all(MG, Executable, Exelines, Flag, Result):
    """
    23.10.6
    将权重和是否经过拆分成两个矩阵，不是经过0.6个，是经过1个，权重变成0.6
    即nv, ns不变
    调整权重步长
    """
    Metric = []
    for _ in range(50):
        metric = []
        for i in range(len(Executable)):
            metric.append([0, 0, 0, 0])  # ev es nv ns
        Metric.append(metric)
    Metric2 = []
    for i in range(len(Executable)):
        Metric2.append([0, 0, 0, 0])  # ev es nv ns
    v = 0
    s = 0
    AllF = 0
    fault = Executable[Flag.index(1)]
    j1 = 0
    c1 = 0
    b1 = 0
    j2 = 0
    c2 = 0
    b2 = 0
    j3 = 0
    c3 = 0
    b3 = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                union = list(set(Exelines[i][j][k][0]) & set(Exelines[i][j][k][1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if len(unique) == 0 or len(union) == 0:
                    continue
                j1 += len(union)
                c1 += len(unique)
                b1 += len(exe)
                if MG[i][j][k] == 1:
                    if not (Result[i][j][k][0] and Result[i][j][k][1] and fault in union):
                        continue
                    j2 += len(union)
                    c2 += len(unique)
                    b2 += len(exe)
                    v += 1
                    if Result[i][j][k][0] and Result[i][j][k][1]:
                        AllF += 1
                    for d in union:
                        index = Executable.index(d)
                        for x in range(25):
                            Metric[x][index][0] += 1  # ev
                        t = 1
                        for y in range(25, 50):
                            Metric[y][index][0] += 1-0.02*t  # ev
                            Metric[y][index][0] = round(Metric[y][index][0], 2)
                            t += 1
                        Metric2[index][0] += 1
                    for d in unique:
                        index = Executable.index(d)
                        t = 1
                        for x in range(25):
                            Metric[x][index][0] += 1-0.02*t  # ev
                            Metric[x][index][0] = round(Metric[x][index][0], 2)
                            t += 1
                        for y in range(25, 50):
                            Metric[y][index][0] += 1  # ev
                        Metric2[index][0] += 1
                elif MG[i][j][k] == 0 or MG[i][j][k] == 3:  # or MG[i][j][k] == 3
                    j3 += len(union)
                    c3 += len(unique)
                    b3 += len(exe)
                    s += 1
                    for d in union:
                        index = Executable.index(d)
                        for x in range(25):
                            Metric[x][index][1] += 1  # ev
                        t = 1
                        for y in range(25, 50):
                            Metric[y][index][1] += 1-0.02*t  # ev
                            Metric[y][index][1] = round(Metric[y][index][1], 2)
                            t += 1
                        Metric2[index][1] += 1
                    for d in unique:
                        index = Executable.index(d)
                        t = 1
                        for x in range(25):
                            Metric[x][index][1] += 1-0.02*t  # ev
                            Metric[x][index][1] = round(Metric[x][index][1], 2)
                            t += 1
                        for y in range(25, 50):
                            Metric[y][index][1] += 1  # ev
                        Metric2[index][1] += 1

    for k in range(50):
        for i in range(len(Metric[k])):
            Metric[k][i][2] = v - Metric2[i][0]
            Metric[k][i][3] = s - Metric2[i][1]
    a = 0
    b = 0
    for i in range(len(Result)):
        for j in range(len(Result[i])):
            for m in range(len(Result[i][j])):
                for n in range(len(Result[i][j][m])):
                    b += 1
                    if Result[i][j][m][n] == 0 and fault in Exelines[i][j][m][n]:
                        a += 1
    EnF = round(a / b * 100, 2)
    SUS = []
    for k in range(50):
        Sus = []
        for t in range(len(Formula)):
            sus = []
            for i in range(len(Metric[k])):
                sus.append(getSus2(Metric[k][i], t, v, s))
            Sus.append(sus)
        SUS.append(Sus)
    if b1 == 0:
        j1p = 0
        c1p = 0
    else:
        j1p = round(j1 / b1 * 100, 2)
        c1p = round(c1 / b1 * 100, 2)
    if v == 0:
        AllF = 0
        j2p = 0
        c2p = 0
    else:
        AllF = round(AllF / v * 100, 2)
        j2p = round(j2 / b2 * 100, 2)
        c2p = round(c2 / b2 * 100, 2)
    if s == 0:
        j3p = 0
        c3p = 0
    else:
        j3p = round(j3 / b3 * 100, 2)
        c3p = round(c3 / b3 * 100, 2)
    Para = [j1p, c1p, j2p, c2p, j3p, c3p, EnF, AllF]
    return SUS, Para, Metric


def Exam(Sus, Flag):
    Sus_c = copy.deepcopy(Sus)
    fault = Flag.index(1)
    EXAM = []
    Maximal = []
    for i in range(len(Sus_c)):
        value = Sus_c[i][fault]
        a = 0
        for j in Sus_c[i]:
            if j > value:
                a += 1
        Sus_c[i].sort(reverse=True)
        index_list = [a for a, b in enumerate(Sus_c[i]) if b == value]
        if len(index_list) > 1:
            # 和fault statement可疑度相等
            b = len(index_list)
            exam = ((a + 1) + (a + b)) / 2
        else:
            exam = a + 1
        max_list = [a for a, b in enumerate(Sus_c[i]) if b == Sus_c[i][0]]
        if len(max_list) > 1:
            # 最大值不止一个
            Max = (1 + len(max_list)) / 2
        else:
            Max = 1
        exam = round(exam / len(Sus_c[0]) * 100, 2)
        Max = round(Max / len(Sus_c[0]) * 100, 2)
        Maximal.append(Max)
        EXAM.append(exam)
    return EXAM, Maximal


def TopN(Sus, Flag, N):
    FLAG = []
    fault = Flag.index(1)
    for i in range(len(Sus)):
        flag = 0
        value = Sus[i][fault]
        a = 0
        for j in Sus[i]:
            if j > value:
                a += 1
        if a >= N:
            # 找不到
            FLAG.append(flag)
        else:
            index_list = [a for a, b in enumerate(Sus[i]) if b == value]
            if a + len(index_list) <= N:
                flag = 1
            else:
                flag = (N-a) / len(index_list)
            FLAG.append(round(flag, 2))
    return FLAG


def getMetrics_1(row, ws, mu, MG, Sus, FaSus, Flag, percent):
    datadict = {}
    tablelist = {"Mutant" + str(mu): ['MS', 'FAILTIM', 'MaximalM', 'MaximalF', 'SMG(%)', 'FS(%)', 'WrongP']}
    datadict.update(tablelist)
    t1 = 0
    t2 = 0
    t3 = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                t3 += 1
                if MG[i][j][k] == 0 or MG[i][j][k] == 3:
                    t1 += 1
                    if MG[i][j][k] == 3:
                        t2 += 1
    if t1 == 0:
        fs = 0
        s = 0
    else:
        fs = round(t2 / t1 * 100, 2)
        s = round(t1 / t3 * 100, 2)

    MSexam, maximalM = Exam(Sus, Flag)
    FAILTIMexam, maximalF = Exam(FaSus, Flag)
    for t in range(len(Formula)):
        value = [MSexam[t], FAILTIMexam[t], maximalM[t], maximalF[t], s, fs, percent]
        data = {
            Formula[t]: value
        }
        datadict.update(data)

    for i, j in datadict.items():  # i--公式名称, j--指标值
        ws.cell(row, 1).value = i  # 添加第 1 列的数据
        for col in range(2, len(j) + 2):  # values列表中索引
            ws.cell(row, col).value = j[col - 2]
        row += 1  # 行数
    row += 2  # 行数
    return row


def getMetrics_2(row, ws, mu, MG, mSus, mSus2, AllF, Flag):
    datadict = {}
    tablelist = {"Mutant" + str(mu): ['MS', 'MS1', 'MS2', 'MS3', 'MS4', 'MS5', 'MS6', 'MS7', 'MS8', 'MS9', 'MS10',
                                      'MaximalM', 'MaximalM1', 'MaximalM2', 'MaximalM3', 'MaximalM4', 'MaximalM5',
                                      'MaximalM6', 'MaximalM7', 'MaximalM8', 'MaximalM9', 'MaximalM10',
                                      'SMG(%)', 'FS(%)', 'AllFofV(%)']}
    datadict.update(tablelist)
    t1 = 0
    t2 = 0
    t3 = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                t3 += 1
                if MG[i][j][k] == 0 or MG[i][j][k] == 3:
                    t1 += 1
                    if MG[i][j][k] == 3:
                        t2 += 1
    if t1 == 0:
        fs = 0
        s = 0
    else:
        fs = round(t2 / t1 * 100, 2)
        s = round(t1 / t3 * 100, 2)
    MSexam, maximalM = Exam(mSus, Flag)
    MS = []
    maximal = []
    for k in range(10):
        MSexam2, maximalM2 = Exam(mSus2[k], Flag)
        MS.append(MSexam2)
        maximal.append(maximalM2)
    for t in range(len(Formula)):
        value = [MSexam[t], MS[0][t], MS[1][t], MS[2][t], MS[3][t], MS[4][t], MS[5][t], MS[6][t], MS[7][t], MS[8][t],
                 MS[9][t], maximalM[t], maximal[0][t], maximal[1][t], maximal[2][t], maximal[3][t], maximal[4][t],
                  maximal[5][t], maximal[6][t], maximal[7][t], maximal[8][t], maximal[9][t], s, fs, AllF]
        data = {
            Formula[t]: value
        }
        datadict.update(data)

    for i, j in datadict.items():  # i--公式名称, j--指标值
        ws.cell(row, 1).value = i  # 添加第 1 列的数据
        for col in range(2, len(j) + 2):  # values列表中索引
            ws.cell(row, col).value = j[col - 2]
        row += 1  # 行数
    row += 2  # 行数
    return row


def getMetrics_3(row, ws, mu, MG, mSus, mSus4, AllF, Flag, Para):
    datadict = {}
    title = ['oms']
    t = 1
    for i in range(25):
        title.append("i1d{}".format(100-t*2))
        t += 1
    t = 1
    for i in range(25):
        title.append("i{}d1".format(100-t*2))
        t += 1
    title.append('SMG')
    title.append('FS')
    title.append('AllFofV')
    title.append('union')
    title.append('unique')
    title.append('unionvmg')
    title.append('uniquevmg')
    tablelist = {"Mutant" + str(mu): title}
    datadict.update(tablelist)
    t1 = 0
    t2 = 0
    t3 = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                t3 += 1
                if MG[i][j][k] == 0 or MG[i][j][k] == 3:
                    t1 += 1
                    if MG[i][j][k] == 3:
                        t2 += 1
    if t1 == 0:
        fs = 0
        s = 0
    else:
        fs = round(t2 / t1 * 100, 2)
        s = round(t1 / t3 * 100, 2)
    MSexam, maximalM = Exam(mSus, Flag)
    MS = []
    maximal = []
    for k in range(50):
        MSexam2, maximalM2 = Exam(mSus4[k], Flag)
        MS.append(MSexam2)
        maximal.append(maximalM2)
    for t in range(len(Formula)):
        value = [MSexam[t]]
        for i in range(50):
            value.append(MS[i][t])
        value.append(s)
        value.append(fs)
        value.append(AllF)
        value.append(Para[0])
        value.append(Para[1])
        value.append(Para[2])
        value.append(Para[3])
        data = {
            Formula[t]: value
        }
        datadict.update(data)

    for i, j in datadict.items():  # i--公式名称, j--指标值
        ws.cell(row, 1).value = i  # 添加第 1 列的数据
        for col in range(2, len(j) + 2):  # values列表中索引
            ws.cell(row, col).value = j[col - 2]
        row += 1  # 行数
    row += 2  # 行数
    return row


def getMetrics_4(row, ws, mu, MG, mSus, mSus4, AllF, Flag, Para, Exelines):
    """
    集成：两种集成策略
    对所有ranking list集成
    对dms和ims分别集成
    """
    datadict = {}
    title = ['oms']
    t = 1
    for i in range(25):
        title.append("i1d{}".format(100-t*2))
        t += 1
    t = 1
    for i in range(25):
        title.append("i{}d1".format(100-t*2))
        t += 1
    title.append('ensemble1')
    title.append('ensemble2')
    title.append('imse1')
    title.append('imse2')
    title.append('dmse1')
    title.append('dmse2')
    title.append('SMG')
    title.append('FS')
    title.append('AllFofV')
    title.append('EnF')
    title.append('union')
    title.append('unique')
    title.append('unionvmg')
    title.append('uniquevmg')
    title.append('unionsmg')
    title.append('uniquesmg')
    tablelist = {"Mutant" + str(mu): title}
    datadict.update(tablelist)
    t1 = 0
    t2 = 0
    t3 = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                union = list(set(Exelines[i][j]) & set(Exelines[i][j * len(MG[0][0]) + k + 1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if len(unique) == 0 or len(union) == 0:
                    continue
                if MG[i][j][k] == 0 or MG[i][j][k] == 1 or MG[i][j][k] == 3:
                    t3 += 1
                    if MG[i][j][k] == 0 or MG[i][j][k] == 3:
                        t1 += 1
                        if MG[i][j][k] == 3:
                            t2 += 1
    if t1 == 0:
        fs = 0
        s = 0
    else:
        fs = round(t2 / t1 * 100, 2)
        s = round(t1 / t3 * 100, 2)
    MSexam, _ = Exam(mSus, Flag)
    # 重新计算可疑度
    # 求每一个语句在每一个列表中的排名
    eSus1 = []
    eSus2 = []
    # 对列表元素进行降序排序，并记录排名
    rank1 = []
    for m in range(len(Formula)):
        rank = []
        for n in range(len(mSus4)):
            r = []
            sorted_list = sorted(mSus4[n][m], reverse=True)
            for i in mSus4[n][m]:
                index = sorted_list.index(i)
                r.append(index)
            rank.append(r)
        rank1.append(rank)
    for i in range(len(rank1)):
        s1 = []
        for k in range(len(rank1[i][0])):
            a = 0
            for j in range(len(rank1[i])):
                a += (len(rank1[i][j]) - rank1[i][j][k])
            s1.append(a/len(rank1[i]))
        eSus1.append(s1)
    mSus4c = copy.deepcopy(mSus4)
    for m in range(len(mSus4)):
        for n in range(len(mSus4[m])):
            min_val = min(mSus4[m][n])
            max_val = max(mSus4[m][n])
            if max_val - min_val == 0:
                pass
            else:
                mSus4c[m][n] = min_max_normalize(mSus4[m][n])
    for m in range(len(mSus4[0])):
        s2 = []
        for n in range(len(mSus4[0][0])):
            a = 0
            for k in range(len(mSus4)):
                a += mSus4c[k][m][n]
            s2.append(a / len(mSus4))
        eSus2.append(s2)
    ims1 = []
    ims2 = []
    dms1 = []
    dms2 = []
    rank1 = []
    rank2 = []
    for m in range(len(Formula)):
        rank = []
        for n in range(25):
            r = []
            sorted_list = sorted(mSus4[n][m], reverse=True)
            for i in mSus4[n][m]:
                index = sorted_list.index(i)
                r.append(index)
            rank.append(r)
        rank1.append(rank)
        rank = []
        for n in range(25, 50):
            r = []
            sorted_list = sorted(mSus4[n][m], reverse=True)
            for i in mSus4[n][m]:
                index = sorted_list.index(i)
                r.append(index)
            rank.append(r)
        rank2.append(rank)
    for i in range(len(rank1)):
        s1 = []
        for k in range(len(rank1[i][0])):
            a = 0
            for j in range(len(rank1[i])):
                a += (len(rank1[i][j]) - rank1[i][j][k])
            s1.append(a/len(rank1[i]))
        ims1.append(s1)
    for i in range(len(rank2)):
        s2 = []
        for k in range(len(rank2[i][0])):
            a = 0
            for j in range(len(rank2[i])):
                a += (len(rank2[i][j]) - rank2[i][j][k])
            s2.append(a/len(rank2[i]))
        dms1.append(s2)
    mSus4c1 = copy.deepcopy(mSus4)
    mSus4c2 = copy.deepcopy(mSus4)
    for m in range(25):
        for n in range(len(mSus4[m])):
            min_val = min(mSus4[m][n])
            max_val = max(mSus4[m][n])
            if max_val - min_val == 0:
                pass
            else:
                mSus4c1[m][n] = min_max_normalize(mSus4[m][n])
    for m in range(25, 50):
        for n in range(len(mSus4[m])):
            min_val = min(mSus4[m][n])
            max_val = max(mSus4[m][n])
            if max_val - min_val == 0:
                pass
            else:
                mSus4c2[m][n] = min_max_normalize(mSus4[m][n])
    for m in range(len(mSus4[0])):
        s2 = []
        for n in range(len(mSus4[0][0])):
            a = 0
            for k in range(25):
                a += mSus4c1[k][m][n]
            s2.append(a / len(mSus4))
        ims2.append(s2)
    for m in range(len(mSus4[0])):
        s2 = []
        for n in range(len(mSus4[0][0])):
            a = 0
            for k in range(25, 50):
                a += mSus4c2[k][m][n]
            s2.append(a / len(mSus4))
        dms2.append(s2)
    MSexame1, _ = Exam(eSus1, Flag)
    MSexame2, _ = Exam(eSus2, Flag)
    MSexame3, _ = Exam(ims1, Flag)
    MSexame4, _ = Exam(ims2, Flag)
    MSexame5, _ = Exam(dms1, Flag)
    MSexame6, _ = Exam(dms2, Flag)
    MS = []
    maximal = []
    for k in range(50):
        MSexam2, maximalM2 = Exam(mSus4[k], Flag)
        MS.append(MSexam2)
        maximal.append(maximalM2)
    for t in range(len(Formula)):
        value = [MSexam[t]]
        for i in range(50):
            value.append(MS[i][t])
        value.append(MSexame1[t])
        value.append(MSexame2[t])
        value.append(MSexame3[t])
        value.append(MSexame4[t])
        value.append(MSexame5[t])
        value.append(MSexame6[t])
        value.append(s)
        value.append(fs)
        value.append(AllF)
        value.append(Para[6])
        value.append(Para[0])
        value.append(Para[1])
        value.append(Para[2])
        value.append(Para[3])
        value.append(Para[4])
        value.append(Para[5])
        data = {
            Formula[t]: value
        }
        datadict.update(data)
    for i, j in datadict.items():  # i--公式名称, j--指标值
        ws.cell(row, 1).value = i  # 添加第 1 列的数据
        for col in range(2, len(j) + 2):  # values列表中索引
            ws.cell(row, col).value = j[col - 2]
        row += 1  # 行数
    row += 2  # 行数
    return row


def getMetrics_5(row, ws, mu, MG, mSus, mSus4, AllF, Flag, Para, Exelines):
    """
    TOP-N
    去掉集成策略
    """
    datadict = {}
    title = ['oms']
    t = 1
    for i in range(25):
        title.append("i1d{}".format(100-t*2))
        t += 1
    t = 1
    for i in range(25):
        title.append("i{}d1".format(100-t*2))
        t += 1
    title.append('SMG')
    title.append('FS')
    title.append('AllFofV')
    title.append('EnF')
    title.append('union')
    title.append('unique')
    title.append('unionvmg')
    title.append('uniquevmg')
    title.append('unionsmg')
    title.append('uniquesmg')
    tablelist = {"Mutant" + str(mu): title}
    datadict.update(tablelist)
    t1 = 0
    t2 = 0
    t3 = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j] + Exelines[i][j * len(MG[0][0]) + k + 1]))
                union = list(set(Exelines[i][j]) & set(Exelines[i][j * len(MG[0][0]) + k + 1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if len(unique) == 0 or len(union) == 0:
                    continue
                if MG[i][j][k] == 0 or MG[i][j][k] == 1 or MG[i][j][k] == 3:
                    t3 += 1
                    if MG[i][j][k] == 0 or MG[i][j][k] == 3:
                        t1 += 1
                        if MG[i][j][k] == 3:
                            t2 += 1
    if t1 == 0:
        fs = 0
        s = 0
    else:
        fs = round(t2 / t1 * 100, 2)
        s = round(t1 / t3 * 100, 2)
    # FLAGset = []
    # for i in [1, 3, 5, 10]:
    #     FLAG = TopN(mSus, Flag, i)
    #     FLAGset.append(FLAG)
    # FLAGset2 = []
    # for i in [1, 3, 5, 10]:
    #     fl = []
    #     for j in mSus4:
    #         FLAG = TopN(j, Flag, i)
    #         fl.append(FLAG)
    #     FLAGset2.append(fl)
    N = 10
    FLAG1 = TopN(mSus, Flag, N)
    FLAG2 = []
    for j in mSus4:
        FLAG = TopN(j, Flag, N)
        FLAG2.append(FLAG)
    for t in range(len(Formula)):
        value = [FLAG1[t]]
        for i in range(50):
            value.append(FLAG2[i][t])
        value.append(s)
        value.append(fs)
        value.append(AllF)
        value.append(Para[6])
        value.append(Para[0])
        value.append(Para[1])
        value.append(Para[2])
        value.append(Para[3])
        value.append(Para[4])
        value.append(Para[5])
        data = {
            Formula[t]: value
        }
        datadict.update(data)
    for i, j in datadict.items():  # i--公式名称, j--指标值
        ws.cell(row, 1).value = i  # 添加第 1 列的数据
        for col in range(2, len(j) + 2):  # values列表中索引
            ws.cell(row, col).value = j[col - 2]
        row += 1  # 行数
    row += 2  # 行数
    return row


def getMetrics_4_grep(row, ws, mu, MG, mSus, mSus4, AllF, Flag, Para, Exelines):
    """
    集成：两种集成策略
    对所有ranking list集成
    对dms和ims分别集成
    """
    datadict = {}
    title = ['oms']
    t = 1
    for i in range(25):
        title.append("i1d{}".format(100-t*2))
        t += 1
    t = 1
    for i in range(25):
        title.append("i{}d1".format(100-t*2))
        t += 1
    title.append('ensemble1')
    title.append('ensemble2')
    title.append('imse1')
    title.append('imse2')
    title.append('dmse1')
    title.append('dmse2')
    title.append('SMG')
    title.append('FS')
    title.append('AllFofV')
    title.append('EnF')
    title.append('union')
    title.append('unique')
    title.append('unionvmg')
    title.append('uniquevmg')
    title.append('unionsmg')
    title.append('uniquesmg')
    tablelist = {"Mutant" + str(mu): title}
    datadict.update(tablelist)
    t1 = 0
    t2 = 0
    t3 = 0
    for i in range(len(MG)):
        for j in range(len(MG[i])):
            for k in range(len(MG[i][j])):
                exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
                union = list(set(Exelines[i][j][k][0]) & set(Exelines[i][j][k][1]))
                unique = [x for x in exe if x not in union]
                exe.sort()
                union.sort()
                if len(unique) == 0 or len(union) == 0:
                    continue
                t3 += 1
                if MG[i][j][k] == 0 or MG[i][j][k] == 3:
                    t1 += 1
                    if MG[i][j][k] == 3:
                        t2 += 1
    if t1 == 0:
        fs = 0
        s = 0
    else:
        fs = round(t2 / t1 * 100, 2)
        s = round(t1 / t3 * 100, 2)
    MSexam, _ = Exam(mSus, Flag)
    # 重新计算可疑度
    # 求每一个语句在每一个列表中的排名
    eSus1 = []
    eSus2 = []
    # 对列表元素进行降序排序，并记录排名
    rank1 = []
    for m in range(len(Formula)):
        rank = []
        for n in range(len(mSus4)):
            r = []
            sorted_list = sorted(mSus4[n][m], reverse=True)
            for i in mSus4[n][m]:
                index = sorted_list.index(i)
                r.append(index)
            rank.append(r)
        rank1.append(rank)
    for i in range(len(rank1)):
        s1 = []
        for k in range(len(rank1[i][0])):
            a = 0
            for j in range(len(rank1[i])):
                a += (len(rank1[i][j]) - rank1[i][j][k])
            s1.append(a/len(rank1[i]))
        eSus1.append(s1)
    mSus4c = copy.deepcopy(mSus4)
    for m in range(len(mSus4)):
        for n in range(len(mSus4[m])):
            min_val = min(mSus4[m][n])
            max_val = max(mSus4[m][n])
            if max_val - min_val == 0:
                pass
            else:
                mSus4c[m][n] = min_max_normalize(mSus4[m][n])
    for m in range(len(mSus4[0])):
        s2 = []
        for n in range(len(mSus4[0][0])):
            a = 0
            for k in range(len(mSus4)):
                a += mSus4c[k][m][n]
            s2.append(a / len(mSus4))
        eSus2.append(s2)
    ims1 = []
    ims2 = []
    dms1 = []
    dms2 = []
    rank1 = []
    rank2 = []
    for m in range(len(Formula)):
        rank = []
        for n in range(25):
            r = []
            sorted_list = sorted(mSus4[n][m], reverse=True)
            for i in mSus4[n][m]:
                index = sorted_list.index(i)
                r.append(index)
            rank.append(r)
        rank1.append(rank)
        rank = []
        for n in range(25, 50):
            r = []
            sorted_list = sorted(mSus4[n][m], reverse=True)
            for i in mSus4[n][m]:
                index = sorted_list.index(i)
                r.append(index)
            rank.append(r)
        rank2.append(rank)
    for i in range(len(rank1)):
        s1 = []
        for k in range(len(rank1[i][0])):
            a = 0
            for j in range(len(rank1[i])):
                a += (len(rank1[i][j]) - rank1[i][j][k])
            s1.append(a/len(rank1[i]))
        ims1.append(s1)
    for i in range(len(rank2)):
        s2 = []
        for k in range(len(rank2[i][0])):
            a = 0
            for j in range(len(rank2[i])):
                a += (len(rank2[i][j]) - rank2[i][j][k])
            s2.append(a/len(rank2[i]))
        dms1.append(s2)
    mSus4c1 = copy.deepcopy(mSus4)
    mSus4c2 = copy.deepcopy(mSus4)
    for m in range(25):
        for n in range(len(mSus4[m])):
            min_val = min(mSus4[m][n])
            max_val = max(mSus4[m][n])
            if max_val - min_val == 0:
                pass
            else:
                mSus4c1[m][n] = min_max_normalize(mSus4[m][n])
    for m in range(25, 50):
        for n in range(len(mSus4[m])):
            min_val = min(mSus4[m][n])
            max_val = max(mSus4[m][n])
            if max_val - min_val == 0:
                pass
            else:
                mSus4c2[m][n] = min_max_normalize(mSus4[m][n])
    for m in range(len(mSus4[0])):
        s2 = []
        for n in range(len(mSus4[0][0])):
            a = 0
            for k in range(25):
                a += mSus4c1[k][m][n]
            s2.append(a / len(mSus4))
        ims2.append(s2)
    for m in range(len(mSus4[0])):
        s2 = []
        for n in range(len(mSus4[0][0])):
            a = 0
            for k in range(25, 50):
                a += mSus4c2[k][m][n]
            s2.append(a / len(mSus4))
        dms2.append(s2)
    MSexame1, _ = Exam(eSus1, Flag)
    MSexame2, _ = Exam(eSus2, Flag)
    MSexame3, _ = Exam(ims1, Flag)
    MSexame4, _ = Exam(ims2, Flag)
    MSexame5, _ = Exam(dms1, Flag)
    MSexame6, _ = Exam(dms2, Flag)
    MS = []
    maximal = []
    for k in range(50):
        MSexam2, maximalM2 = Exam(mSus4[k], Flag)
        MS.append(MSexam2)
        maximal.append(maximalM2)
    for t in range(len(Formula)):
        value = [MSexam[t]]
        for i in range(50):
            value.append(MS[i][t])
        value.append(MSexame1[t])
        value.append(MSexame2[t])
        value.append(MSexame3[t])
        value.append(MSexame4[t])
        value.append(MSexame5[t])
        value.append(MSexame6[t])
        value.append(s)
        value.append(fs)
        value.append(AllF)
        value.append(Para[6])
        value.append(Para[0])
        value.append(Para[1])
        value.append(Para[2])
        value.append(Para[3])
        value.append(Para[4])
        value.append(Para[5])
        data = {
            Formula[t]: value
        }
        datadict.update(data)
    for i, j in datadict.items():  # i--公式名称, j--指标值
        ws.cell(row, 1).value = i  # 添加第 1 列的数据
        for col in range(2, len(j) + 2):  # values列表中索引
            ws.cell(row, col).value = j[col - 2]
        row += 1  # 行数
    row += 2  # 行数
    return row


def getMetrics_5_grep(row, ws, mu, MG, mSus, mSus4, AllF, Flag, Para, Exelines):
    """
    TOP-N
    去掉集成策略
    """
    datadict = {}
    title = ['oms']
    t = 1
    for i in range(25):
        title.append("i1d{}".format(100-t*2))
        t += 1
    t = 1
    for i in range(25):
        title.append("i{}d1".format(100-t*2))
        t += 1
    # title.append('SMG')
    # title.append('FS')
    title.append('AllFofV')
    title.append('EnF')
    title.append('union')
    title.append('unique')
    title.append('unionvmg')
    title.append('uniquevmg')
    title.append('unionsmg')
    title.append('uniquesmg')
    tablelist = {"Mutant" + str(mu): title}
    datadict.update(tablelist)
    t1 = 0
    t2 = 0
    t3 = 0
    # for i in range(len(MG)):
    #     for j in range(len(MG[i])):
    #         for k in range(len(MG[i][j])):
    #             exe = list(set(Exelines[i][j][k][0] + Exelines[i][j][k][1]))
    #             union = list(set(Exelines[i][j][k][0]) & set(Exelines[i][j][k][1]))
    #             unique = [x for x in exe if x not in union]
    #             exe.sort()
    #             union.sort()
    #             if len(unique) == 0 or len(union) == 0:
    #                 continue
    #             t3 += 1
    #             if MG[i][j][k] == 0 or MG[i][j][k] == 3:
    #                 t1 += 1
    #                 if MG[i][j][k] == 3:
    #                     t2 += 1
    # if t1 == 0:
    #     fs = 0
    #     s = 0
    # else:
    #     fs = round(t2 / t1 * 100, 2)
    #     s = round(t1 / t3 * 100, 2)
    N = 10
    FLAG1 = TopN(mSus, Flag, N)
    FLAG2 = []
    for j in mSus4:
        FLAG = TopN(j, Flag, N)
        FLAG2.append(FLAG)
    for t in range(len(Formula)):
        value = [FLAG1[t]]
        for i in range(50):
            value.append(FLAG2[i][t])
        # value.append(s)
        # value.append(fs)
        value.append(AllF)
        value.append(Para[6])
        value.append(Para[0])
        value.append(Para[1])
        value.append(Para[2])
        value.append(Para[3])
        value.append(Para[4])
        value.append(Para[5])
        data = {
            Formula[t]: value
        }
        datadict.update(data)
    for i, j in datadict.items():  # i--公式名称, j--指标值
        ws.cell(row, 1).value = i  # 添加第 1 列的数据
        for col in range(2, len(j) + 2):  # values列表中索引
            ws.cell(row, col).value = j[col - 2]
        row += 1  # 行数
    row += 2  # 行数
    return row


import math


class Mutant3:
    def Determinant(self, A, n):
        f1 = f2 = f3 = f4 = True  # 分别标识4种三角矩阵
        symbol = 0
        for i in range(n):
            for j in range(n):
                if f1 and j > i and A[i * n + j] != 0:
                    f1 = False
                if f2 and i > j and A[i * n + j] != 0:
                    f2 = False
                if f3 and i + j < n - 1 and A[i * n + j] != 0:
                    f3 = False
                if f4 and i + j > n - 1 and A[i * n + j] != 0:
                    f4 = False
        if f1 or f2:  # 主对角线含有非0元素的三角矩阵
            result = 1
            for i in range(n):
                result *= A[i * n]  # result *= A[i*n+i]  --> result *= A[i*n]
                symbol = 1
            return result, symbol
        elif f3 or f4:  # 次对角线含有非0元素的三角矩阵(主对角线全0)
            result = int(math.pow(-1, n * (n - 1) / 2))
            for i in range(n):
                result *= A[i * n + (n - 1 - i)]
            return result, symbol
        else:  # 展开法求行列式值
            return self.DeterComp(A, n), symbol

    def DeterComp(self, A, n):
        mid = 0
        temp = []
        for i in range(n * n):
            temp.append(A[i])
        if n == 1:
            result = A[0]
        else:
            for i in range(n):
                mid += int(math.pow(-1, 2 + i)) * A[i] * self.DeterComp(self.AlgComp(temp, n, i), n - 1)
            result = mid
        return result

    def AlgComp(self, x, n, i):
        array = []
        for j in range(n, n * n):
            if j % n == i:
                pass
            else:
                array.append(x[j])
        return array


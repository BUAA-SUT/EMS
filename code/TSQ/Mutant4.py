import math


class Mutant4:
    def trisquare(self, argv):
        symbol = 0  # 检查测试用例是否经过了错误语句
        area = 0
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b:
            print('Not a triangle')
            return area, symbol
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if pow(Max, 2) < pow(mid, 2) + pow(Min, 2):  # 锐角三角形
            # print('Acute triangle')
            if Max == mid:  # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))
                area = Min * h / 2
                return area, symbol
            elif Min == mid:  # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                area = Max * h / 2
                return area, symbol
            else:  # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) / 2
                area = math.sqrt(p * (p - Max) * (p - mid) * (p - Min))
                return area, symbol
        if pow(Max, 2) == pow(mid, 2) + pow(Min, 2):  # 直角三角形
            # print('Right-angled triangle')
            area = mid * Min  # mid*Min/2
            symbol = 1
            return area, symbol
        # print('Obtuse triangle')
        if Min == mid:  # 钝角等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            area = Max * h / 2
            return area, symbol
        else:  # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            area = Max * h / 2
            return area, symbol


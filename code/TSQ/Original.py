import math


class Trisquare:
    def trisquare(self, argv):
        symbol = 0  # 检查测试用例是否经过了错误语句
        a = argv[0]
        b = argv[1]
        c = argv[2]
        if a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b:
            print('Not a triangle')
            return 0
        Sum = a + b + c
        Max = max(a, b, c)
        Min = min(a, b, c)
        mid = Sum - Max - Min
        if pow(Max, 2) < pow(mid, 2) + pow(Min, 2):
            # 锐角三角形
            if Max == mid:
                # 顶角小于或等于60度的等腰三角形
                h = math.sqrt(pow(Max, 2) - pow(Min / 2, 2))
                return Min * h / 2, symbol
            elif Min == mid:
                # 顶角大于60度的等腰三角形
                h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
                return Max * h / 2, symbol
            else:
                # 不规则的锐角三角形，海伦公式计算
                p = (Max + mid + Min) / 2
                return math.sqrt(p * (p - Max) * (p - mid) * (p - Min)), symbol
        if pow(Max, 2) == pow(mid, 2) + pow(Min, 2):
            # 直角三角形
            return mid * Min / 2, symbol
        if Min == mid:
            # 钝角等腰三角形
            h = math.sqrt(pow(Min, 2) - pow(Max / 2, 2))
            return Max * h / 2, symbol
        else:
            # 不规则钝角三角形，Max乘以高除以2
            x = (pow(Max, 2) + pow(mid, 2) - pow(Min, 2)) / (2 * Max)
            h = math.sqrt(pow(mid, 2) - pow(x, 2))
            return Max * h / 2, symbol


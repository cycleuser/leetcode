
class Solution:
    # 定义一个解决类，用于实现计算从X到Y所需操作次数的方法

    def brokenCalc(self, X: int, Y: int) -> int:
        # 计算将X变为Y所需的最小按键次数
        res = 0
        # 初始化结果计数器为0
        
        while X < Y:
            if Y % 2 == 0:
                Y //= 2  # 如果Y是偶数，直接除以2
            else:
                Y += 1   # 如果Y是奇数，加1使其变为偶数再除以2
            res += 1    # 每次操作计数器加1
        
        return res + X - Y  # 返回总操作次数加上X和Y的差值



class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        res = 0
        while X < Y:
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
            res += 1
        
        return res + X - Y


class Solution:
    def findIntegers(self, num):
        """
        :param num: 输入的整数 (integer)
        :return: 满足条件的整数个数 (满足条件的整数数量)

        该函数用于计算给定二进制表示中，不包含连续两个 '1' 的子序列个数。
        """

        # 将十进制转换为二进制字符串，并去除前缀 '0b'
        num, sub = bin(num)[2:], 0
        # 初始化两个数组用于存放以 '0' 和 '1' 开头的合法序列数量
        zero, one = [1] * len(num), [1] * len(num)

        for i in range(1, len(num)):
            # 根据前一个状态更新当前位置的状态数
            zero[i], one[i] = zero[i - 1] + one[i - 1], zero[i - 1]

        for i in range(1, len(num)):
            # 如果找到连续两个 '1'，停止循环
            if num[i] == num[i - 1] == "1": break
            # 计算不包含连续零的子序列个数
            if num[i] == num[i - 1] == "0":
                sub += one[-1 - i]

        return zero[-1] + one[-1] - sub

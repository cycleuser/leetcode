
class Solution:
    # 初始化数字字典和字符串长度
    def __init__(self):
        self.dic = {str(i): i for i in range(10)}

    def multiply(self, num1: str, num2: str) -> str:
        """
        :param num1: 第一个乘数，字符串形式
        :param num2: 第二个乘数，字符串形式
        :return: 两个乘数的积，字符串形式
        """
        
        # 计算每个数字在各自位置上的值，并求和转换成整数
        n1 = sum(self.dic[n] * (10 ** (len(num1) - i - 1)) for i, n in enumerate(num1))
        n2 = sum(self.dic[n] * (10 ** (len(num2) - j - 1)) for j, n in enumerate(num2))

        # 计算乘积并返回结果
        return str(n1 * n2)

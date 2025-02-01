
class Solution:
    # 定义一个类来实现求幂操作

    def myPow(self, x: float, n: int) -> float:
        """
        :param x: 基数，浮点数类型
        :param n: 指数，整型
        :return: 计算结果为浮点数

        采用快速幂算法来计算x的n次方
        """
        if n < 0:
            # 如果指数为负，则将指数取反，并用1/x替换基数
            n *= -1
            x = 1 / x
        
        elif not n:
            # 如果指数为零，返回1（任何数的0次方都是1）
            return 1
        
        half = self.myPow(x, n // 2)
        # 计算x^(n//2)的结果
        return x * half * half if n % 2 else half * half
        # 如果n是偶数，直接返回half*half；否则返回x*half*half

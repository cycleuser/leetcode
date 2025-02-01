
class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 初始化各个位置的计数器
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1

        for _ in range(N - 1):
            # 更新各个位置的计数器值
            x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = \
                (x6 + x8), (x7 + x9), (x4 + x8), \
                (x7 + x9 + x0), 0, (x1 + x7 + x0), \
                (x2 + x6), (x1 + x7), (x2 + x4), \
                (x4 + x6)
        
        # 返回结果模数
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10 ** 9 + 7)

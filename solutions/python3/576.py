
from collections import defaultdict

class Solution:
    def __init__(self):
        """初始化字典用于存储中间结果"""
        self.dic = defaultdict(int)

    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        """
        :param m: 行数
        :param n: 列数
        :param N: 步数
        :param i: 起始行位置
        :param j: 起始列位置
        :return: 在给定步数内到达边界次数（模10^9+7）
        """
        
        # 检查是否超出边界或步数为负
        if N >= 0 and (i < 0 or j < 0 or i >= m or j >= n):
            return 1

        # 如果步数小于0，返回0
        elif N < 0:
            return 0
        
        # 如果当前状态已计算过，则直接返回结果
        elif (i, j, N) not in self.dic:
            for p in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                self.dic[(i, j, N)] += self.findPaths(m, n, N - 1, i + p[0], j + p[1])

        # 返回结果取模
        return self.dic[(i, j, N)] % (10 ** 9 + 7)

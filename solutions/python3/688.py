
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        """
        计算骑士在N×N棋盘上经过K步后，停留在指定位置的概率。
        
        :param N: 棋盘的大小
        :param K: 骑士移动的步数
        :param r: 起始行坐标
        :param c: 起始列坐标
        :return: 骑士在K步后停留在给定位置的概率
        
        使用记忆化递归（Memoization）来加速计算过程。
        """
        
        memo = {}
        
        def dfs(i, j, p, k):
            # 如果当前位置在棋盘内且剩余步数小于总步数
            if 0 <= i < N and 0 <= j < N and k < K:
                sm = 0
                # 骑士的所有可能移动方向
                for x, y in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)):
                    # 如果该位置和步数组合未被计算过
                    if (i + x, j + y, k) not in memo:
                        # 记录并计算结果
                        memo[(i + x, j + y, k)] = dfs(i + x, j + y, p / 8, k + 1)
                    sm += memo[(i + x, j + y, k)]
                return sm
            else:
                # 如果当前位置超出棋盘边界或步数用尽，则返回0或当前位置的概率（1）
                return 0 <= i < N and 0 <= j < N and p or 0
        
        # 初始位置和概率为1，剩余步数为0
        return dfs(r, c, 1, 0)

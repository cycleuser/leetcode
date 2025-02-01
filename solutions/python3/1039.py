
class Solution:
    # 定义一个解决方案类
    
    def minScoreTriangulation(self, A: List[int]) -> int:
        """
        计算将给定的三角形顶点A进行最优三角剖分后的最小得分。
        
        参数:
            A (List[int]): 三角形的顶点数组
        
        返回值:
            int: 最小得分
        """
        memo = {}
        # 使用字典存储已经计算过的子问题结果，避免重复计算

        def dp(i, j):
            """
            动态规划函数，用于计算从索引i到j之间的最优三角剖分的最小得分。
            
            参数:
                i (int): 当前考虑的起始顶点
                j (int): 当前考虑的结束顶点
            
            返回值:
                int: 从i到j间的最小得分
            """
            if (i, j) not in memo:
                # 如果(i,j)不在memo中，表示还未计算过该子问题
                memo[i, j] = min([dp(i, k) + dp(k, j) + A[i] * A[j] * A[k] for k in range(i + 1, j)] or [0])
                # 对于所有可能的分割点k，递归计算最小得分并存储在memo中
            return memo[i, j]
        # 调用dp函数从索引0到len(A)-1开始计算总最小得分
        
        return dp(0, len(A) - 1)

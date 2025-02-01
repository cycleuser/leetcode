
class Solution:
    # 定义石子游戏II的解决方案类

    def stoneGameII(self, A: List[int]) -> int:
        N = len(A)
        
        # 从后向前累加数组元素，使得A[i]表示从前i个元素开始可以得到的最大分数和
        for i in range(N - 2, -1, -1):
            A[i] += A[i + 1]
        
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(i, m):
            # 如果当前索引加上m的两倍已经超过数组长度，直接返回当前累积值
            if i + 2 * m >= N: 
                return A[i]
            
            # 计算以i为起点，选择不同步长x（1到2*m）能获得的最大分数，并取最小值减去当前累加和作为结果
            return A[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        
        # 调用动态规划函数从索引0开始，初始步长为1
        return dp(0, 1)

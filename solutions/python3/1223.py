
class Solution:
    def dieSimulator(self, n: int, r: List[int]) -> int:
        """
        n: 模拟投掷的次数
        r: 等概率投掷结果的最大值，即骰子面数
        
        返回：n次投掷后点数之和的所有可能组合数量对 10^9 + 7 取模的结果
        """
        
        K = max(r)  # 骰子最大点数
        dp = [[[0 for k in range(K)] for j in range(6)] for i in range(n)]
        
        # 初始化基础状态：第一次投掷每个面出现的概率为1，且点数为0的情况只有一种
        for j in range(6):
            dp[0][j][0] = 1
        
        # 动态规划填表过程
        for i in range(1, n):
            for j in range(6):
                # 计算当前状态在点数为0的情况下的值
                dp[i][j][0] += sum(dp[i-1][t][k] for t in range(6) for k in range(r[t]) if t != j)
                
                # 计算当前状态在点数大于0的情况下的值，即上一次投掷的相同点数
                for k in range(1, r[j]):
                    dp[i][j][k] = dp[i-1][j][k-1]
        
        # 结果计算：所有可能组合数量求和对 10^9 + 7 取模
        return sum(dp[n-1][j][k] for j in range(6) for k in range(K)) % (10**9+7)

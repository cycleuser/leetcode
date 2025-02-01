
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        """
        计算在游戏新21点规则下赢得概率
        
        Args:
            N (int): 可以尝试的最大数值
            K (int): 游戏开始时的初始值
            W (int): 累计和窗口大小

        Returns:
            float: 赢得游戏的概率
        """
        
        if K == 0 or N >= K + W:
            # 如果K为0或N大于等于K+W，直接返回1表示必赢
            return 1
        
        dp = [1.0] + [0.0] * N  # 初始化动态规划表
        Wsum, res = 1.0, 0.0   # 累积和与结果初始化
        
        for i in range(1, N + 1):
            # 更新dp[i]
            dp[i] += Wsum / W
            if i < K: 
                # 如果i小于K，累积和Wsum加上当前概率dp[i]
                Wsum += dp[i]
            else:
                # 否则结果res累加当前概率dp[i]
                res += dp[i]
            
            if i - W >= 0: 
                # 当i-W大于等于0时，从累积和中减去dp[i-W]以维护窗口大小
                Wsum -= dp[i - W]
        
        return res

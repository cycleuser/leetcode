
class Solution:
    def probabilityOfHeads(self, p: List[float], t: int) -> float:
        """
        计算在给定每个硬币正面概率p的情况下，恰好投掷t次得到正面的概率。

        参数：
            p: List[float] - 每个硬币投掷正面的概率列表
            t: int         - 需要恰好得到的正面次数

        返回值:
            float - 得到确切t次正面的概率
        """
        
        n = len(p)  # 硬币数量
        
        # 初始化动态规划表，dp[i][j] 表示使用前i个硬币得到j次正面的所有可能方式的累积概率
        dp = [[0.0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # 空集情况下，没有硬币时恰好得到0次正面的概率为1
        
        # 动态规划计算过程
        for i in range(1, n + 1):
            for j in range(i + 1):
                if j == 0:
                    # 使用前i个硬币恰好得到0次正面，只有不使用第i个硬币的情况
                    dp[i][j] = dp[i - 1][j] * (1.0 - p[i - 1])
                else: 
                    # 使用前i个硬币恰好得到j次正面，分为两部分：第i个硬币反面和正面
                    dp[i][j] = (dp[i - 1][j] * (1.0 - p[i - 1])) + (dp[i - 1][j - 1] * p[i - 1])
        
        # 返回最后结果，即使用所有硬币恰好得到t次正面的概率
        return dp[-1][t]

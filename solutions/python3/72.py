
class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        """
        计算两个字符串的最小编辑距离。
        
        参数:
            w1 (str): 第一个源字符串
            w2 (str): 第二个目标字符串
        
        返回:
            int: 最小编辑距离
        """
        # 初始化动态规划表
        dp = [[0] * (len(w2) + 1) for i in range(len(w1) + 1)]
        
        # 填充第一行和第一列
        for i in range(len(w1) + 1):
            dp[i][0] = i
        for j in range(len(w2) + 1):
            dp[0][j] = j
        
        # 动态规划计算最小编辑距离
        for i in range(1, len(w1) + 1):
            for j in range(1, len(w2) + 1):
                if w1[i - 1] == w2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        
        return dp[-1][-1]


class Solution:
    # 定义一个类来解决最长公共子序列问题

    def longestCommonSubsequence(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        # 初始化动态规划表，大小为 (m+1) x (n+1)，初始值为 0
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        
        # 遍历字符串 a 和 b 的每个字符
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果当前字符相同，则dp[i][j] = dp[i-1][j-1] + 1
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 否则，dp[i][j] 取上一状态的最大值
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        # 返回动态规划表右下角的值，即最长公共子序列的长度
        return dp[-1][-1]

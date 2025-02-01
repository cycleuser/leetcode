
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 初始化动态规划表，用于存储子问题的解
        dp = [[0 for j in range(len(s))] for i in range(len(s))]
        
        # 从后往前遍历字符串，确保dp[i+1][j-1]已经计算过
        for i in range(len(s) - 1, -1, -1):
            # 每个字符单独作为一个回文子序列的最小情况
            dp[i][i] = 1
            
            # 遍历字符串的后半部分，避免重复计算
            for j in range(i + 1, len(s)):
                # 如果当前字符和对称位置的字符相等，则长度+2
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # 否则取左右子序列的最大值
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # 返回最长回文子序列的长度
        return dp[0][len(s) - 1]

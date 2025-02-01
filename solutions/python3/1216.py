
class Solution:
    # 判断字符串s在删除最多k个字符后是否能成为回文串
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        
        # 初始化动态规划表，dp[i][j]表示前i和前j个字符需要删除的最小次数使得它们相同
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # 动态规划填充
        for i in range(1, n + 1): 
            for j in range(1, n + 1):
                if not i or not j: 
                    dp[i][j] = i or j  # 边界条件：空字符串与非空字符串需要删除的字符次数
                elif s[i - 1] == s[n - j]: 
                    dp[i][j] = dp[i - 1][j - 1]  # 字符相同，不需要额外删除
                else: 
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])  # 删除一个字符的情况
        
        # 如果需要删除的最小次数不大于2*k，则可以成为回文串
        return dp[n][n] <= k * 2


class Solution:
    # 计算两个字符串的最长公共子序列(LCS)
    def compute_lcs(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        dp = [[""] * (n + 1) for _ in range(m + 1)]  # 初始化动态规划表
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] != t[j - 1]:  # 如果字符不同
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)  # 取最长的子序列
                else:  # 如果字符相同
                    dp[i][j] = dp[i - 1][j - 1] + s[i - 1]  # 延续之前的子序列
        
        return dp[-1][-1]  # 返回LCS

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        lcs = self.compute_lcs(str1, str2)
        
        ans = []
        i, j = 0, 0
        m, n = len(str1), len(str2)
        
        # 遍历LCS中的每个字符ch
        for ch in lcs:
            while i < m and str1[i] != ch: 
                ans.append(str1[i])
                i += 1
            while j < n and str2[j] != ch: 
                ans.append(str2[j])
                j += 1
            
            # 添加当前字符ch，并更新指针i和j
            ans.append(ch)
            i += 1
            j += 1
        
        return ''.join(ans) + str1[i:] + str2[j:]

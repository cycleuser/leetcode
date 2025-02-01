
class Solution:
    def strangePrinter(self, s: str) -> int:
        """
        Strange Printer problem solution.
        
        参数:
        s (str): 输入字符串
        
        返回:
        int: 打印s所需最少操作次数
        """
        memo = {}
        
        def dp(i: int, j: int) -> int:
            """
            Dynamic programming function to calculate minimum operations needed.

            参数:
            i (int): 起始索引
            j (int): 结束索引

            返回:
            int: 从i到j所需的最少操作次数
            """
            if i > j:
                return 0
            if (i, j) not in memo:
                ans = dp(i + 1, j) + 1
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        ans = min(ans, dp(i, k - 1) + dp(k + 1, j))
                memo[i, j] = ans
            return memo[i, j]
        
        return dp(0, len(s) - 1)

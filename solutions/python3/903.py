
class Solution:
    def numPermsDISequence(self, S: str) -> int:
        """
        计算满足给定序列的排列数。
        
        参数:
            S: 字符串，表示递增("I")和递减("D")序列
        
        返回:
            满足条件的排列数 % (10^9 + 7)
        """
        dp = [1] * (len(S) + 1)
        
        # 遍历字符串S
        for c in S:
            if c == "I":
                # 处理递增序列
                dp = dp[:-1]
                for i in range(1, len(dp)):
                    dp[i] += dp[i - 1]
            else:
                # 处理递减序列
                dp = dp[1:]
                for i in range(len(dp) - 1)[::-1]:
                    dp[i] += dp[i + 1]
        return dp[0] % (10**9 + 7)

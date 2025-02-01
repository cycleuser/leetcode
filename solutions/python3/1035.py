
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        """
        使用动态规划解决最长公共子序列问题，从而计算最大不相交线的数量。
        
        :param A: List[int], 第一个整数数组
        :param B: List[int], 第二个整数数组
        :return: int, 最大不相交线数量
        
        例如:
            A = [1,4,2]
            B = [1,2,4]
            返回结果为: 2
        """
        
        dp, m, n = collections.defaultdict(int), len(A), len(B)
        # 动态规划表初始化
        for i in range(m):
            for j in range(n):
                # 计算当前位置的最大值，考虑匹配与否
                dp[i, j] = max(dp[i - 1, j - 1] + (A[i] == B[j]), dp[i - 1, j], dp[i, j - 1])
        return dp[m - 1, n - 1]


class Solution:
    # 定义一个类，用于解决给定数组A在分割K个子区间后的最大和问题

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        # 初始化动态规划表dp，大小为N+K
        dp = [0] * (N + K)

        for i in range(N):
            # 当前最大值初始化为0
            curMax = 0
            # 遍历可能的分割长度k，范围从1到min(K, i+1)
            for k in range(1, min(K, i + 1) + 1):
                # 更新当前子区间内的最大值
                curMax = max(curMax, A[i - k + 1])
                # 动态规划更新：选择当前分割方式的最大收益
                dp[i] = max(dp[i], dp[i - k] + curMax * k)

        # 返回最终结果，即dp[N-1]
        return dp[N - 1]

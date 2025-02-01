
class Solution:
    def mergeStones(self, stones, K):
        """
        Chinese: 
        给定一个包含非负整数的数组，表示一些石头的位置。你需要合并这些石头，每次可以合并连续K个石头。
        如果最终能将所有石头合并为一个，则返回所需的最小代价；否则返回-1。

        English:
        Given an array of non-negative integers, representing some stone positions.
        You need to merge these stones. Each time you can merge K consecutive stones into one.
        If all the stones can be merged into one in the end, return the minimum cost; otherwise, return -1.
        """

        n = len(stones)
        if (n - 1) % (K - 1): 
            # Chinese: 如果合并后的石头数量不能被K-1整除，则无法完成合并，直接返回-1
            # English: If the number of merged stones cannot be divided by K-1, return -1 as it's impossible to merge all.
            return -1

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools
        # Chinese: 使用lru_cache来缓存dp函数的结果，避免重复计算
        # English: Use lru_cache to cache the result of dp function to avoid redundant calculations
        @functools.lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K:
                # Chinese: 当区间长度小于K时，无需合并操作，直接返回0
                # English: If the length of the interval is less than K, no merge operation needed, return 0.
                return 0

            res = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, K - 1))
            if (j - i) % (K - 1) == 0:
                # Chinese: 如果当前区间可以被完全合并，则加上该区间的总和
                # English: If the current interval can be fully merged, add its total sum.
                res += prefix[j + 1] - prefix[i]
            return res

        return dp(0, n - 1)

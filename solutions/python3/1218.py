
from collections import Counter

class Solution:
    # 定义一个解决方案类来解决最长等差子序列问题
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        # 使用Counter来记录以每个元素结尾的最长等差子序列长度
        dp = Counter()
        
        for a in arr:
            # 更新当前元素a在dp中的值为之前其前驱元素(a-d)对应的值+1，取最大值
            dp[a] = max(dp[a], dp[a - d] + 1)
        
        # 返回所有记录的最大值，即最长等差子序列的长度
        return max(dp.values())


from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        """
        初始化一个defaultdict来存储差值和对应索引下的最大长度
        - 使用defaultdict来自动处理不存在的键，默认值为0，便于后续直接取值
        """
        dp = defaultdict(int)
        
        """
        遍历列表A中的每个元素对（i, j），j > i，
        计算差值 b - a，并更新dp表中该差值对应的最长等差子序列长度
        """
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a, b = A[i], A[j]
                dp[b - a, j] = max(dp[b - a, j], dp[b - a, i] + 1)
        
        """
        返回dp表中所有值的最大值加一，即为最长等差子序列的长度
        - 加一是因为初始长度至少为2（自身和下一个数）
        """
        return max(dp.values()) + 1


class Solution:
    # 判断给定的序列是否可以分割成至少K个连续子序列，每个子序列包含相同的元素

    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        # 计算每个数字出现的最大次数
        max_count = max(collections.Counter(nums).values())
        
        # 检查是否可以分割成至少K个子序列
        return K * max_count <= len(nums)

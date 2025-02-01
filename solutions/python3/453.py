
class Solution:
    # 计算将所有数组元素变为相同值所需的最小移动次数
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 总和减去最小值的n倍，即为解
        return sum(nums) - min(nums) * len(nums)

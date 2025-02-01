
class Solution:
    # 判断给定列表 nums 中是否存在两个不同的索引 i 和 j，使得 nums[i] == nums[j] 且 abs(i - j) <= k

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 使用字典记录每个数字最后出现的位置
        dic = {}
        for i, num in enumerate(nums):
            # 检查当前数字是否已经存在于字典中，并且索引差值小于等于k
            if num in dic and i - dic[num] <= k:
                return True
            # 更新字典记录当前数字的最新位置
            dic[num] = i
        # 如果遍历完整个列表都没有找到符合条件的情况，则返回False
        return False

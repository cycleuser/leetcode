
class Solution:
    # 定义一个类，用于解决附近近乎重复元素的问题

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        判断在数组nums中是否存在两个不同的索引i和j使得 |i - j| <= k 且 |nums[i] - nums[j]| <= t
        :param nums: List[int], 输入的整数列表
        :param k: int, 索引差的最大值限制
        :param t: int, 数字差的最大值限制
        :return: bool, 如果存在这样的两个元素返回True，否则返回False
        """
        if t < 0:
            # 时间复杂度为O(n)，空间复杂度为O(min(n, k))，其中n是数组的长度
            return False
        
        d = {}
        for i in range(len(nums)):
            m = nums[i] // (t + 1)
            # 检查当前元素是否接近已存在的桶中的元素
            if m in d or (m - 1 in d and nums[i] - d[m - 1] <= t) or (m + 1 in d and d[m + 1] - nums[i] <= t):
                return True
            # 将当前元素放入对应桶中
            d[m] = nums[i]
            # 移除超出窗口范围的元素
            if i >= k:
                del d[nums[i - k] // (t + 1)]
        return False

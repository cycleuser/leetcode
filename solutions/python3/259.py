
class Solution:
    # 定义一个类用于解决三个数之和小于目标值的问题

    def threeSumSmaller(self, nums, target):
        """
        计算数组中三个元素之和小于给定目标值的三元组个数
        
        :param nums: List[int] - 一个整数列表
        :param target: int - 目标和
        :return: int - 满足条件的三元组数量
        """
        # 首先对数组进行排序，方便后续双指针操作
        nums.sort()
        
        res = 0
        # 遍历每个可能的第一个元素
        for i in range(len(nums) - 2):
            r = len(nums) - 1
            # 确定第二个和第三个元素的位置，并使用双指针优化搜索过程
            for j in range(i + 1, len(nums) - 1):
                while r > j + 1 and nums[i] + nums[j] + nums[r] >= target:
                    r -= 1
                # 当找到满足条件的组合时，计数并调整指针位置
                if nums[i] + nums[j] + nums[r] < target:
                    res += r - j
        return res

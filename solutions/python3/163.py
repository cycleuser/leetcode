
class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        寻找缺失的数字范围

        :param nums: 整数数组
        :param lower: 区间下限
        :param upper: 区间上限
        :return: 缺失的数字范围列表
        """
        if not nums:
            # 如果nums为空，直接返回一个缺失范围或单独缺失的数字
            return [f"{lower}->{upper}"] if lower != upper else [str(lower)]
        
        res, n = [], len(nums)
        # 处理区间起点前的缺失情况
        if lower + 1 < nums[0]:
            res.append(f"{lower}->{nums[0] - 1}")
        elif lower + 1 == nums[0]:
            res.append(str(lower))
        
        # 遍历数组，找到并记录中间和结尾的缺失区间
        for i in range(1, n):
            if nums[i] > nums[i - 1] + 2:
                res.append(f"{nums[i - 1] + 1}->{nums[i] - 1}")
            elif nums[i] == nums[i - 1] + 2:
                res.append(str(nums[i] - 1))
        
        # 处理区间结尾后的缺失情况
        if nums[-1] + 1 < upper:
            res.append(f"{nums[-1] + 1}->{upper}")
        elif nums[-1] + 1 == upper:
            res.append(str(upper))
        
        return res

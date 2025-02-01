
class Solution:
    # 类名：Solution

    def missingNumber(self, nums):
        """
        :param nums: 数组，包含从0到n-1的整数，但缺少一个数字
        :return: 缺失的那个数字
        
        解题思路：
        1. 利用等差数列求和公式计算0到n-1的总和。
        2. 计算给定数组nums中所有元素之和。
        3. 两者的差值即为缺失的数字。    
        """
        # 计算0到len(nums)的等差数列总和
        total_sum = len(nums) * (len(nums) + 1) // 2
        
        # 计算数组nums中所有元素之和
        actual_sum = sum(nums)
        
        # 返回缺失的数字
        return total_sum - actual_sum

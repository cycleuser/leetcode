
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 对数字列表进行排序，以方便获取最大值和最小值
        # Sort the numbers to easily access max and min values
        nums.sort()
        
        # 计算最后三个数的乘积和第一个数与前两个最小数的乘积的最大值
        # Calculate the maximum product of the last three or first two minimums and one maximum value
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])


class Solution:
    # 计算将数组中的所有元素移动到中间值所需的最小移动次数

    def minMoves2(self, nums):
        # 首先对数组进行排序
        nums.sort()

        # 找到中位数，对于奇数长度的数组，中位数是中间的那个数；
        # 对于偶数长度的数组，中位数可以是中间两个数中的任何一个
        m = nums[(len(nums) - 1) // 2]

        # 计算所有元素移动到中位数所需的操作次数总和
        return sum(abs(num - m) for num in nums)

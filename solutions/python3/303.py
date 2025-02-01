
class NumArray:

    # 初始化类，传入一个整数列表nums
    # 中文: 初始化类，传入一个整数列表nums
    # 英文: Initialize the class with a list of integers nums

    def __init__(self, nums):
        self.nums = nums  # 存储输入的数字列表
        # 中文: 存储输入的数字列表
        # English: Store the input list of numbers
        
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i - 1]
        # 中文: 使用前缀和优化求区间和
        # 英文: Use prefix sum to optimize range sum queries

    def sumRange(self, i, j):
        return self.nums[j] - self.nums[i - 1] if i else self.nums[j]
        # 中文: 返回从索引i到j的区间和
        # 英文: Return the sum of elements from index i to j

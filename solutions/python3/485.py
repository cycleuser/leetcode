
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]  # 输入列表nums，元素为整数
        :rtype: int            # 返回最大连续1的数量
        """
        cons = [0, 0]  # 初始化计数器数组，[当前最大长度, 当前连续1的长度]
        
        for num in nums:
            if num == 1:  # 如果当前数字是1
                cons[1] += 1  # 更新当前连续1的数量
            else:  # 否则，重置当前连续1的数量
                cons[1] = 0
            cons[0] = max(cons[0], cons[1])  # 更新最大连续1的长度
        
        return cons[0]  # 返回最大连续1的长度

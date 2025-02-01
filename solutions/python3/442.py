
class Solution:
    # 寻找数组中重复的元素 - Find duplicates in the array

    def findDuplicates(self, nums):
        """
        :type nums: List[int]  # 输入参数：整数列表
        :rtype: List[int]      # 返回类型：整数列表，包含所有重复的数字
        """
        out = list()  # 存储结果 - Store the result
        
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                out.append(abs(nums[i]))  # 如果该位置数值小于0，则表示之前已经访问过，加入结果列表
            else:
                nums[abs(nums[i]) - 1] *= -1  # 将对应位置的数取反，标记为已访问
        
        return out  # 返回最终的结果列表 - Return the final result list


class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]  # 输入参数，整数列表
        :rtype: int          # 返回类型，最长连续递增子序列的长度
        """
        if not nums: return 0  # 如果输入列表为空，返回0
        
        curr, mx = 1, 1  # 初始化当前计数和最大值为1

        for i in range(len(nums) - 1):  # 遍历整个列表（除了最后一个元素）
            if nums[i + 1] > nums[i]:  # 如果后一个数字大于前一个数字
                curr += 1  # 当前计数加1
                mx = max(mx, curr)  # 更新最大值
            else:
                curr = 1  # 重置当前计数为1
        
        return mx  # 返回最长连续递增子序列的长度

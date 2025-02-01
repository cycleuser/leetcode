
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        输入目标和s以及数组nums，返回满足条件的最小子数组长度。
        
        :param s: int 目标和
        :param nums: List[int] 数组元素
        :return: int 满足条件的最小子数组长度，若无则返回0
        """
        l, res, curr = 0, len(nums) + 1, 0  # 初始化左指针l、结果res和当前子数组和curr
        
        for r, num in enumerate(nums):  # 遍历数组nums的每个元素，索引为r，值为num
            curr += num  # 更新当前子数组和curr
            
            while curr >= s:  # 当前子数组和大于等于目标和s时
                res, l, curr = min(res, r - l + 1), l + 1, curr - nums[l]  # 更新结果res，右移左指针l并更新当前子数组和curr
        
        return res < len(nums) + 1 and res or 0  # 返回满足条件的最小子数组长度

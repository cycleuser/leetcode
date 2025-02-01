
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :param nums: List[int] - 输入数组
        :param k: int - 乘积限制值
        :return: int - 满足条件的子数组数量
        """
        
        l, res, cur = 0, 0, 1  # 初始化左边界，结果计数器和当前乘积累积
        
        for i in range(len(nums)):
            cur *= nums[i]  # 将当前元素加入累积乘积
            
            while cur >= k and l < i:  # 当累积乘积大于等于k且左边界未到右边界时
                cur //= nums[l]  # 移除左边界元素，更新累积乘积
                l += 1  # 左边界右移
                
            if cur < k:  # 如果当前累积乘积仍小于k
                res += i - l + 1  # 更新结果计数器
            
        return res  # 返回满足条件的子数组数量

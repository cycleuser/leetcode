
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        计算每个索引位置的元素乘积，但不包括该位置的元素
        
        1. 初始化乘积结果和临时存储
            m = 1  # 用于累乘前半部分数组
            res = []  # 存储结果

        2. 遍历数组计算前缀积并存入结果列表中
            对于每个元素，将其左侧所有元素的积累乘到m中，并将当前的m值存入结果列表
        
        3. 初始化右半部分的累积乘积为1
            m = 1  # 用于累乘后半部分数组

        4. 反向遍历数组，更新每个位置的结果为前缀积 * 后缀积
            对于每个元素，将其右侧所有元素的积累乘到m中，并与结果列表中的值相乘
        
        5. 返回最终结果
            返回累乘后的结果列表res
        """
        m, res = 1, []
        
        # 计算前缀积
        for i in range(len(nums)):
            res.append(m)
            m *= nums[i]
        
        # 更新每个位置的结果为前缀积 * 后缀积
        m = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= m
            m *= nums[i]
            
        return res

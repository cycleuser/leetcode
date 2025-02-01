
class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 如果列表只有一个数字，直接返回该数字的字符串形式
        if len(nums) == 1:
            return str(nums[0])
        
        # 如果列表有两个数字，返回两个数字用 '/' 连接的结果
        elif len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        
        # 对于长度大于2的列表，优化表达式以最大化除法运算结果
        else:
            # 使用 join 方法将剩余元素组合成一个字符串，并在每个元素之间插入 '/'
            inner_part = "/".join(str(i) for i in nums[1:])
            # 返回第一个数字与括号内其他元素组合后的最终表达式
            return str(nums[0]) + "/(" + inner_part + ")"

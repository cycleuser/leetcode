
class Solution:
    # 类：Solution
    
    def checkPossibility(self, nums):
        """
        :type nums: List[int]  # 输入类型：整数列表
        :rtype: bool           # 返回类型：布尔值
        
        目标：检查给定的整数列表是否可以通过修改最多一个元素使其变为非递减序列。
        策略：
            - 遍历整个列表，寻找首次出现的不满足条件的位置 i 使得 nums[i] > nums[i+1]
            - 尝试两种可能的修正方案：(i) 删除 nums[i] (ii) 删除 nums[i+1]
            - 检查这两种修正后的序列是否为非递减
        """
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                # 两种修正尝试
                mod1, mod2 = list(nums), list(nums)
                mod1[i], mod2[i+1] = mod1[i+1], mod2[i]
                
                # 检查是否可以通过删除一个元素使其变为非递减序列
                if sorted(mod1) != mod1 and sorted(mod2) != mod2:
                    return False
        
        # 如果未发现违反规则的情况，返回 True
        return True

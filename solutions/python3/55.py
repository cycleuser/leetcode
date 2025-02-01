
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 初始化当前能到达的最大索引 mx 和起始位置 i
        i = mx = 0
        
        # 当 i 小于数组长度且 i 不大于最大可到达索引 mx 时，继续循环
        while i < len(nums) and i <= mx:
            # 如果从当前位置可以跳到最后一个元素或更远，则返回 True
            if nums[i] + i >= len(nums) - 1: 
                return True
            
            # 更新能到达的最大索引 mx 为 max(mx, 当前位置加跳跃距离)
            mx = max(mx, i + nums[i])
            
            # 移动到下一个位置 i+1
            i += 1
        
        # 如果跳出循环且无法跳到最后一个元素，则返回 False
        return False


class Solution:
    # 定义一个类来解决寻找数组的“平衡索引”问题

    def pivotIndex(self, nums: List[int]) -> int:
        # 计算整个数组元素之和
        sm = sum(nums)
        
        cur = 0  # 当前累积和
        
        for i in range(len(nums)):
            # 如果当前累积和等于剩余部分的总和，返回索引i
            if cur == sm - cur - nums[i]:
                return i
            
            # 更新当前累积和
            cur += nums[i]
        
        # 如果没有找到平衡索引，则返回-1
        return -1

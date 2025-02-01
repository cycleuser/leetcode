
class Solution:
    # 定义一个类来解决子数组和的问题

    def subarraySum(self, nums, k):
        # 初始化字典用于存储累积和的出现次数，结果计数器以及当前累积和
        sums, res, sm = {}, 0, 0
        
        for i in range(len(nums)):
            # 更新字典中的累积和出现次数，并计算当前元素加入后的新的累积和
            sums[sm], sm = (sums[sm] + 1 if sm in sums else 1), sm + nums[i]
            
            # 如果当前累积和减去目标值 k 在字典中存在，则累加计数器
            if sm - k in sums: res += sums[sm - k]
        
        return res  # 返回结果计数器的值，即满足条件的子数组数量

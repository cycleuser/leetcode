
class Solution:
    # 定义一个解决方案类

    def majorityElement(self, nums):
        # 寻找数组中出现次数超过总数三分之一的元素（摩尔投票法）
        c1, c2, cnt1, cnt2 = 0, 1, 0, 0
        # 初始化候选元素和计数器，c1 和 c2 分别为两个候选值，cnt1 和 cnt2 用于统计候选值的出现次数
        
        for num in nums:
            if num == c1:
                cnt1 += 1
            elif num == c2:
                cnt2 += 1
            # 如果当前数字等于c1，则增加c1的计数；如果等于c2，则增加c2的计数
            
            elif not cnt1:
                c1, cnt1 = num, 1
            elif not cnt2:
                c2, cnt2 = num, 1
            # 如果cnt1为0，说明候选元素c1已经失效，选择当前数字作为新的候选元素，并初始化其计数器；相同逻辑处理c2
            
            else:
                cnt1 -= 1
                cnt2 -= 1
            # 其余情况下，减少两个候选值的计数
        
        return [c for c in (c1, c2) if nums.count(c) > len(nums) // 3]
        # 返回满足条件的最终候选元素（出现次数超过总数三分之一）

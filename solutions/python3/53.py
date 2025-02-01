
class Solution:
    # 定义一个类来解决问题

    def maxSubArray(self, nums):
        # 初始化当前和、最小前缀和、最大子数组和为0，负无穷大
        sm, mn, mx = 0, 0, -float("inf")
        
        for num in nums:
            # 累加当前数字到总和中
            sm += num
            
            # 更新最大子数组和，采用动态规划的思想
            mx, mn = max(mx, sm - mn), min(mn, sm)
        
        # 返回最终的最大子数组和
        return mx

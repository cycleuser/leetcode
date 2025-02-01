
class Solution:
    # 定义一个类来解决删除并获得最大值的问题

    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        
        cnt, dp, maxs = Counter(nums), {}, {}  # 统计每个数字的出现次数，初始化动态规划字典dp和最大值字典maxs
        nums = sorted(set(nums))  # 对nums去重并排序

        if len(nums) < 2:
            return nums and nums[0] * cnt[nums[0]] or 0  # 如果数字少于两个，直接返回第一个数的累积值
        
        for i in range(len(nums)):
            dp[i] = nums[i] * cnt[nums[i]]  # 计算当前数字累积值并存入dp
            
            if i >= 2:
                if nums[i - 1] < nums[i] - 1:  # 检查是否可以累加
                    dp[i] += maxs[i - 1]
                else:
                    dp[i] += maxs[i - 2]
                maxs[i] = max(dp[i], maxs[i - 1])  # 更新最大值字典
            
            elif i:
                if nums[i - 1] < nums[i] - 1:  # 检查是否可以累加
                    dp[i] += dp[i - 1]
                maxs[i] = max(dp[i], dp[i - 1])  # 更新最大值字典
            
            else:
                maxs[i] = dp[i]  # 初始化第一个位置的最大值
        
        return max(dp[len(nums) - 1], dp[len(nums) - 2])  # 返回最后两个累积值中的较大者

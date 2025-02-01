
class Solution:
    # 寻找最长递增子序列的数量
    
    def findNumberOfLIS(self, nums):
        """
        :param nums: List[int]
        :return: int
        
        使用动态规划记录每个位置的最长递增子序列长度及其数量。
        1. dp[j][0] 表示以 j 结尾的 LIS 长度
           dp[j][1] 表示以 j 结尾且长度为 dp[j][0] 的 LIS 的数量
        
        对于每一个 nums[i]，遍历其后续元素 nums[j] (j > i)：
            - 如果 nums[j] > nums[i]，说明可以构成递增子序列
              更新 dp[j]：如果当前以 i 结尾的 LIS 长度大于等于 j 位置的，则更新长度和数量
                          如果当前以 i 结尾的 LIS 长度加一等于 j 位置的，则增加数量
        
        最后，将所有 LIS 的长度排序并返回最长递增子序列的数量
        """
        
        dp = [[1, 1] for _ in range(len(nums))]  # 初始化动态规划表
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    if dp[i][0] >= dp[j][0]: 
                        dp[j] = [dp[i][0] + 1, dp[i][1]]
                    elif dp[i][0] == dp[j][0] - 1: 
                        dp[j][1] += dp[i][1]
        
        # 排序后计算结果
        dp.sort()
        return sum(d[1] for d in dp if d[0] == dp[-1][0]) or 0

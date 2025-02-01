
class Solution:
    # 定义一个类来解决任务调度问题

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # 将开始时间、结束时间和利润组合成元组并按结束时间排序，以优化计算
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        
        # 初始化动态规划表 dp，表示以当前时间为界的最大收益
        dp = [[0, 0]]
        
        for s, e, p in jobs:
            # 使用二分查找找到第一个大于等于开始时间的结束时间的位置 i
            i = bisect.bisect(dp, [s + 1]) - 1
            
            # 如果当前任务在之前的最大收益基础上增加的利润更大，则更新 dp 表
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        
        # 返回最终的最大收益
        return dp[-1][1]

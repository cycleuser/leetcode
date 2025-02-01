
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        """
        如果航班或假期天数为空，返回0
        :param flights: 航班可用性矩阵
        :param days: 每个城市的假期天数组成的列表
        :return: 最大可利用的假期天数
        """

        if not flights or not days:
            return 0

        n, k = len(flights), len(days[0])  # 城市数量和假期天数
        dp = [[-1] * (k + 1) for _ in range(n)]  # 动态规划数组，初始化为-1

        # 初始状态：在第一个城市，第0天开始度假
        dp[0][0] = 0

        # 遍历每一天和每个城市
        for w in range(1, k + 1):
            for c in range(n):

                # 计算当前城市当前天数的最大假期天数
                max_days = -1
                for pre in range(n):  # 遍历所有可能的前一个城市

                    if (flights[pre][c] or pre == c) and dp[pre][w - 1] >= 0:  # 如果可以到达当前城市或者在原地
                        max_days = max(max_days, dp[pre][w - 1] + days[c][w - 1])

                dp[c][w] = max_days

        # 返回所有城市的最大假期天数
        return max(dp[c][-1] for c in range(n))

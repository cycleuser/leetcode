
class Solution:
    # 定义一个解决方案类

    def maxProfit(self, prices):
        # 初始化动态规划变量：dp1表示持有股票的最大利润，dp2表示首次卖出股票后的最大利润，
        #                dp3表示第二次买入股票后的最大累计亏损（负值）

        dp1, dp2, dp3 = 0, 0, -float("inf")
        
        for p in prices:
            # 遍历每一天的价格
            
            # 更新持有股票的最大利润
            dp1, dp2, dp3 = dp3 + p, max(dp1, dp2), max(dp2 - p, dp3)
            # 依次更新dp1, dp2, dp3
        
        return max(dp1, dp2)  # 返回最大利润

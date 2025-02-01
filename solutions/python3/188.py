
class Solution:
    # 定义一个解决最大利润问题的类
    
    def maxProfit(self, k, prices):
        """
        :param k: 可以进行的最大交易次数
        :param prices: 股票价格列表
        :return: 最大可能盈利
        
        中文注释:
        1. 如果可以进行的交易次数k大于等于股票天数的一半，则可以直接在所有正收益的日子里买卖，直接求和即可。
        2. 否则需要动态规划来计算最大利润。
        
        英文注释:
        1. If the maximum number of transactions k is greater than or equal to half the length of the prices list, 
           we can make transactions in all days with positive profits by summing them up.
        2. Otherwise, use dynamic programming to calculate the maximum profit.
        """
        
        if k >= len(prices) // 2:
            # 如果交易次数k大于等于价格列表长度的一半
            return sum(sell - buy for sell, buy in zip(prices[1:], prices[:-1]) if sell - buy > 0)
        
        dp = [[0, -float("inf")] for _ in range(k + 1)]
        # 初始化动态规划表，dp[i][0] 表示第i次交易的最大利润
        # dp[i][1] 表示第i次交易后的最大亏损
        
        for p in prices:
            for i in range(k + 1):
                if i and dp[i - 1][1] + p > dp[i][0]:
                    # 更新dp表，如果当前价格加上上次交易的亏损大于等于当前的最大利润，则更新
                    dp[i][0] = dp[i - 1][1] + p 
                if dp[i][0] - p > dp[i][1]:
                    # 更新最大亏损记录
                    dp[i][1] = dp[i][0] - p
        
        return dp[-1][0]
        # 返回最后一次交易的最大利润

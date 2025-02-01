
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 初始化状态：持有股票时的最大利润为负无穷，未持有股票时的最大利润为0
        dp = [-float('inf'), 0]
        
        # 遍历每一天的价格
        for p in prices:
            # 更新持有股票和未持有股票两种状态下的最大利润
            x = max(dp[1] - p, dp[0])
            y = max(dp[1], dp[0] + p)
            dp = [x, y]
        
        # 返回最后一天结束时，不持有股票的最大利润
        return dp[-1]

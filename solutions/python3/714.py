
class Solution:
    # 定义一个解决方案类

    def maxProfit(self, prices, fee):
        # prices: 价格列表，代表每天的股票价格
        # fee: 每次交易的手续费
        
        pre = [0, -float("inf")]  # 初始化前一个状态：持有现金（p0）和持有股票（p1）
        
        for p in prices:
            # 更新当前状态
            p0, p1 = pre[1] + p - fee, pre[0] - p
            
            if p0 > pre[0]:  # 如果卖出并扣除手续费后获得的现金更多，则更新持有现金的状态
                pre[0] = p0
            
            if p1 > pre[1]:  # 如果买入股票获得更多，更新持有股票的状态
                pre[1] = p1
        
        return pre[0]  # 返回最终持有的最大现金量

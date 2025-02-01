
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]  # 输入参数：价格列表
        :rtype: int           # 返回类型：最大利润（整数）
        """
        # 差分列表，初始值为0
        diff_list = [0, 0]
        
        for i in range(1, len(prices)):
            # 判断当前价格与前一价格的差值加上前一状态的差值是否大于等于0
            if prices[i] - prices[i-1] + diff_list[1] >= 0:
                # 更新当前状态为新的差值，可能包含之前的累积正收益
                diff_list[1] = prices[i] - prices[i-1] + diff_list[1]
                # 更新历史最大利润
                diff_list[0] = max(diff_list[0], diff_list[1])
            else:
                # 如果当前价格下降，则重置差分状态为0
                diff_list[1] = 0
        
        return diff_list[0]  # 返回计算得到的最大利润

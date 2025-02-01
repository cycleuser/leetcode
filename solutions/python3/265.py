
class Solution:
    # 定义一个名为Solution的类，用于解决给定的最小成本问题

    def minCostII(self, costs):
        # 计算每一轮中从上一层到当前层的成本最低路径
        
        for i in range(1, len(costs)):
            for j in range(len(costs[0])):
                # 对于每一行，更新当前房屋的最小成本
                # 通过加上前一行除自身外其他颜色的最小值来更新当前颜色的成本
                costs[i][j] += min(costs[i - 1][:j] + costs[i - 1][j + 1:])
        
        # 返回最后一层的所有成本中的最小值，如果costs为空，则返回0
        return costs and min(costs[-1]) or 0


class Solution:
    # 定义一个解决方案类

    def minCostClimbingStairs(self, cost):
        """
        :param cost: List[int] - 代表每个台阶的成本列表
        :return: int - 到达最后一级台阶的最小成本
        
        思路：通过动态规划，从第三个台阶开始计算到当前台阶的最小成本
              更新cost数组以减少空间复杂度
        """
        
        for i in range(2, len(cost)):
            # 从第三个台阶开始更新每个台阶的成本为到达该台阶的最小代价
            cost[i] += min(cost[i - 1], cost[i - 2])
        
        # 返回最后两个台阶中的较小值，因为可以从倒数第一个或倒数第二个台阶跳到最后一个台阶
        return min(cost[-1], cost[-2])

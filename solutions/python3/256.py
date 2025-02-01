
class Solution:
    # 定义一个类来解决问题，使用动态规划解决最小成本路径问题

    def minCost(self, costs: List[List[int]]) -> int:
        # 初始化一个长度为3的dp数组，用于记录每种颜色的成本
        dp = [0] * 3
        
        # 遍历每一栋房子的颜色成本
        for a, b, c in costs:
            # 计算重新涂成绿色、蓝色和红色时所需的最小成本
            c1 = min(dp[1], dp[2]) + a
            c2 = min(dp[0], dp[2]) + b
            c3 = min(dp[0], dp[1]) + c
            
            # 更新dp数组，存储最新的成本值
            dp = [c1, c2, c3]
        
        # 返回最终的最小成本
        return min(dp)

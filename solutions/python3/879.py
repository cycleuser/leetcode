
class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        """
        计算在给定限制下，可获利的方案数量。
        
        参数：
            G (int): 最大团队人数限制
            P (int): 利润目标
            group (List[int]): 每个团队的人数
            profit (List[int]): 每个团队的预期利润
        
        返回值:
            int: 在给定限制下，可获利的方案数量
        """
        
        # 动态规划表初始化
        dp = [[0] * (G + 1) for _ in range(P + 1)]
        # 起始状态：无团队时利润为0且人数为0的情况只有一种方案
        dp[0][0] = 1
        
        # 遍历每个团队和对应的预期利润及人数
        for p, g in zip(profit, group):
            # 从利润目标倒序遍历，确保已计算过的状态可用
            for i in range(P, -1, -1):
                # 从最大团队人数减去当前团队的人数开始反向遍历，保证数据正确更新
                for j in range(G - g, -1, -1):
                    # 更新dp表中的状态值
                    dp[min(i + p, P)][j + g] += dp[i][j]
        
        # 返回满足条件的所有方案总数模数结果
        return sum(dp[P]) % (10**9 + 7)

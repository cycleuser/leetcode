
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: list[tuple[int]]) -> int:
        """
        N: 地图的大小，正方形网格。
        mines: 矿点的位置列表，矿点不能被覆盖。

        返回：可以放置“+”的最大长度（边长）。
        """

        # 初始化动态规划表 dp 和结果 res
        # mines 转换为集合便于快速查找
        dp, res, mines = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)], 0, {(i, j) for i, j in mines}

        # 计算每个位置的上、左方向的最大覆盖长度
        for i in range(N):
            for j in range(N):
                if (i, j) not in mines:
                    try:
                        dp[i][j][0] = dp[i - 1][j][0] + 1
                    except:
                        dp[i][j][0] = 1
                    try:
                        dp[i][j][1] = dp[i][j - 1][1] + 1
                    except:
                        dp[i][j][1] = 1

        # 计算每个位置的下、右方向的最大覆盖长度，并更新最大结果 res
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if (i, j) not in mines:
                    try:
                        dp[i][j][2] = dp[i + 1][j][2] + 1
                    except:
                        dp[i][j][2] = 1
                    try:
                        dp[i][j][3] = dp[i][j + 1][3] + 1
                    except:
                        dp[i][j][3] = 1
                    res = max(res, min(dp[i][j]))

        return res

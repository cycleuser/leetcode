
class Solution:
    # Python 解决方案

    def uniquePaths(self, m: int, n: int) -> int:
        """
        计算从左上角到右下角的不同路径数。

        参数:
        m (int): 列的数量。
        n (int): 行的数量。

        返回:
        int: 不同路径的总数。
        """

        # 动态规划数组，用于存储每个位置的路径数量
        dp = [[0] * m for _ in range(n)]

        # 起始点的路径数为1
        dp[0][0] = 1

        # 填充动态规划表
        for i in range(n):
            for j in range(m):
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]

        # 返回右下角的路径数，即为不同路径总数
        return dp[-1][-1]


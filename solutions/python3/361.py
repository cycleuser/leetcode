
class Solution:
    # 初始化解决方案类

    def maxKilledEnemies(self, grid):
        m, n, res = len(grid), len(grid and grid[0]), 0  # 获取行数m和列数n，初始化结果res为0
        dp = [[[0, 0, 0, 0] for j in range(n + 1)] for i in range(m + 1)]  # 初始化动态规划表dp
        
        # 从左上到右下遍历网格
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    dp[i][j][0] = dp[i][j - 1][0]  # 左侧相同行的敌人数量
                    dp[i][j][1] = dp[i - 1][j][1]  # 上方相同列的敌人数量
                elif grid[i][j] == "E":
                    dp[i][j][0] = dp[i][j - 1][0] + 1  # 左侧相同行增加一个敌人
                    dp[i][j][1] = dp[i - 1][j][1] + 1  # 上方相同列增加一个敌人
        
        # 从右下到左上反向遍历网格，更新dp表
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == "0":
                    dp[i][j][2] = dp[i][j + 1][2]  # 右侧相同行的敌人数量
                    dp[i][j][3] = dp[i + 1][j][3]  # 下方相同列的敌人数量
                elif grid[i][j] == "E":
                    dp[i][j][2] = dp[i][j + 1][2] + 1  # 右侧相同行增加一个敌人
                    dp[i][j][3] = dp[i + 1][j][3] + 1  # 下方相同列增加一个敌人

                if grid[i][j] == "0":
                    res = max(res, sum(dp[i][j]))  # 更新最大敌人数量结果
        
        return res

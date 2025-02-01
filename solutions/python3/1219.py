
class Solution:
    # 定义求最大黄金路径的方法
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        # 深度优先搜索辅助函数，用于递归寻找路径
        def dfs(i: int, j: int, value: int) -> None:
            seen.add((i, j))  # 标记当前位置已经访问过
            dp[i][j] = max(dp[i][j], value)  # 更新当前位置的最大值

            # 遍历四个方向的邻居节点
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] > 0 and (x, y) not in seen:
                    dfs(x, y, value + grid[x][y])  # 继续深度优先搜索
            seen.discard((i, j))  # 从已访问集合中移除当前节点
        
        m, n = len(grid), len(grid[0])  # 获取行数和列数
        dp = [[0] * n for _ in range(m)]  # 初始化动态规划表

        # 遍历整个网格，寻找起点并进行深度优先搜索
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    seen = set()  # 每次新的路径开始时清空已访问集合
                    dfs(i, j, grid[i][j])  # 开始深度优先搜索
        
        return max(c for row in dp for c in row)  # 返回最大黄金值

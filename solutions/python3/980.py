
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        # 深度优先搜索函数，参数为当前坐标 (i, j) 和已访问过的空地数量 visited
        def dfs(i, j, visited):
            if grid[i][j] == 2:
                # 到达目标位置，检查是否所有空地都被访问过
                self.walks += visited == self.visit
                return

            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                # 检查边界和障碍物
                if 0 <= x < m and 0 <= y < n and grid[x][y] != -1:
                    grid[i][j] -= 1  # 标记当前位置为已访问或非空地，防止重复访问
                    dfs(x, y, visited + 1)
                    grid[i][j] += 1  # 还原现场

        m, n = len(grid), len(grid[0])  # 获取网格的行数和列数
        self.visit = m * n - sum(c == -1 for row in grid for c in row)  # 计算需要访问的空地数量
        self.walks = 0

        # 遍历整个网格，寻找起点并进行深度优先搜索
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] -= 1  # 标记起点为已访问或非空地
                    dfs(i, j, 1)  # 调用深度优先搜索函数
        return self.walks

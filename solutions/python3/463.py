
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        计算岛屿的周长

        Parameters:
            grid (List[List[int]]): 二维网格，1表示陆地，0表示水域
        
        Returns:
            int: 岛屿的周长
        """

        self.res = 0  # 初始化结果变量
        used = set()  # 记录已访问的位置

        def dfs(i, j):
            """
            深度优先搜索计算单个岛屿的周长

            Parameters:
                i (int): 当前行索引
                j (int): 当前列索引
            """
            used.add((i, j))  # 标记当前位置为已访问
            self.res += 4  # 每遇到一个陆地，初始周长加4

            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    self.res -= 1  # 邻近陆地减少一条边
                    if (x, y) not in used:
                        dfs(x, y)  # 继续递归搜索

        m, n = len(grid), len(grid[0])  # 获取网格的行数和列数
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in used:
                    dfs(i, j)  # 从未访问的陆地开始搜索

        return self.res  # 返回计算得到的周长


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        (中文)求解岛屿的最大面积。
        
        参数：
            - grid: List[List[int]] - 二维网格，1表示陆地，0表示水
        
        返回值：
            最大岛屿面积（整数）
        """

        m, n = len(grid), len(grid and grid[0])
        # (英文) 获取网格的行数和列数
        def explore(i, j):
            """
            (中文) 递归探索陆地并标记为已访问。
            
            参数：
                - i: int - 当前行索引
                - j: int - 当前列索引

            返回值：
                当前岛屿的面积（整数）
            """
            grid[i][j] = 0  # (英文) 将当前位置标记为已访问，避免重复计算
            return 1 + sum(explore(x, y) for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
                           if 0 <= x < m and 0 <= y < n and grid[x][y])
        # (英文) 对于每个单元格，如果为陆地则开始探索并计算岛屿面积
        return max(grid[i][j] and explore(i, j) or 0 for i in range(m) for j in range(n))

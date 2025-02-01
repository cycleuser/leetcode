
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        """
        Solution class for coloring the border of a given cell in a grid.
        
        Parameters:
            - grid (List[List[int]]): The input grid.
            - r0 (int): Row index of the starting cell.
            - c0 (int): Column index of the starting cell.
            - color (int): New color to be applied.

        Returns:
            - List[List[int]]: The updated grid with colored borders.
        """
        
        def dfs(i, j):
            # 记录已访问的单元格
            seen.add((i, j))
            # 如果当前单元格不是目标颜色或周围没有完全相同的目标颜色，则着色
            if not (0 < i < m - 1 and 0 < j < n - 1 and grid[i - 1][j] == grid[i + 1][j] == grid[i][j - 1] == grid[i][j + 1] == self.tar):
                matrix[i][j] = 0
            # 遍历当前单元格的四个方向
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == self.tar and (x, y) not in seen:
                    dfs(x, y)
        
        # 获取网格的行数和列数
        m, n = len(grid), len(grid[0])
        # 记录已访问的单元格
        seen = set()
        # 目标颜色
        self.tar = grid[r0][c0]
        # 深拷贝原始网格用于着色
        matrix = [row[:] for row in grid]
        
        # 从起始点进行深度优先搜索
        dfs(r0, c0)
        
        # 遍历更新后的矩阵，对边界单元格进行颜色填充
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[i][j] = color
        
        return matrix

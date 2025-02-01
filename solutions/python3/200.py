
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        计算给定二维网格中岛屿的数量。
        
        参数：
            - grid : List[List[str]] -- 给定的二维网格
        
        返回值：
            int -- 岛屿的数量
        """
        if not grid or len(grid) == 0:
            return 0
        
        res, n, m = 0, len(grid), len(grid[0])
        
        def explore(i: int, j: int):
            """
            使用深度优先搜索探索岛屿。
            
            参数：
                - i : int -- 行索引
                - j : int -- 列索引
            """
            grid[i][j] = "-1"
            if i > 0 and grid[i - 1][j] == "1": explore(i - 1, j)
            if j > 0 and grid[i][j - 1] == "1": explore(i, j - 1)
            if i + 1 < n and grid[i + 1][j] == "1": explore(i + 1, j)
            if j + 1 < m and grid[i][j + 1] == "1": explore(i, j + 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    explore(i, j)
                    res += 1

        return res


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        初始化腐烂橘子的起始位置，并使用广度优先搜索（BFS）来模拟感染过程。
        
        :param grid: 二维列表，表示橘子的状态，0 表示空地，1 表示新鲜橘子，2 表示腐烂橘子
        :return: 返回腐烂所需的时间，如果所有橘子都腐烂则返回时间，否则返回 -1
        
        初始化腐烂橘子的起始位置和计时器 t、网格大小 m 和 n。
        """
        bfs, t, m, n = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 2], 0, len(grid), len(grid[0])
        
        while bfs:
            # 新一轮的腐烂橘子
            new = []
            
            # 遍历当前轮次中的所有腐烂橘子
            for i, j in bfs:
                # 检查四个方向上的邻近位置
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        # 邻近的新鲜橘子腐烂
                        grid[x][y] = 2
                        new.append((x, y))
            
            bfs = new
            # 如果有新的腐烂橘子加入，则计时器 t 加一
            t += bool(bfs)
        
        # 检查所有橘子是否都已腐烂
        return t if all(val != 1 for row in grid for val in row) else -1

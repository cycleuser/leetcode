
class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        """
        给定一个二维网格，计算不同的岛屿数量。
        1. 判断矩阵是否为空或行数、列数为0，为空则返回0.
        2. 扩展矩阵边界以避免越界检查.
        3. 初始化集合存储已经遇到的岛屿形态，并计数器记录不同岛屿的数量.
        
        使用广度优先搜索遍历每个陆地块并标记访问过的陆地。将当前岛屿形态添加到结果集中，计算不同的形态数量。
        """
        if not grid or not grid[0]: 
            return 0
        m, n = len(grid), len(grid[0])

        # 扩展矩阵边界以避免越界检查
        grid.append([0] * n)
        for row in grid: 
            row.append(0)

        self.pool = set()
        self.res = 0

        def bfs(i0, j0):
            """
            广度优先搜索，从起点i0,j0开始，标记访问过的陆地并扩展岛屿边界。
            将形态存储到结果集中，并计算不同岛屿的总数。
            """
            grid[i0][j0] = -1
            q = [(i0, j0)]
            for i, j in q:
                for I, J in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                    if grid[I][J] == 1:
                        grid[I][J] = -1
                        q.append((I,J))
            self.addisland(q)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    bfs(i, j)
        
        return self.res

    def addisland(self, q):
        """
        将当前岛屿形态添加到结果集，计算不同岛屿的总数。
        通过旋转和镜像操作对岛屿进行标准化处理，避免重复计数。
        """
        Imin = min(x for x,y in q)
        Jmin = min(y for x,y in q)
        
        # 对岛屿进行坐标偏移，原点移到左下角
        island1 = tuple(sorted((x-Imin, y-Jmin) for x,y in q))
        
        if island1 in self.pool:
            return None
        
        self.res += 1

        Imax = max(x for x,y in island1)
        Jmax = max(y for x,y in island1)

        # 镜像变换
        island2 = tuple(sorted((-x+Imax, y) for x,y in island1))
        island3 = tuple(sorted((x,-y+Jmax) for x,y in island1))
        island4 = tuple(sorted((-x+Imax,-y+Jmax) for x,y in island1))

        # 对角线变换
        island5 = tuple(sorted((y, x) for x,y in island1))
        island6 = tuple(sorted((-x+Jmax, y) for x,y in island5))
        island7 = tuple(sorted((x,-y+Imax) for x,y in island5))
        island8 = tuple(sorted((-x+Jmax,-y+Imax) for x,y in island5))

        self.pool |= set([island1, island2, island3, island4, island5, island6, island7, island8])

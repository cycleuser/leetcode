
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        这个方法用来计算给定网格中两个最近陆地格子之间的最大距离。
        
        :param grid: 网格，由 0 和 1 组成的二维列表
        :return: 返回两个最近陆地格子之间的最大距离
        
        思路：
        1. 使用队列进行广度优先搜索（BFS）。
        2. 初始化一个队列 q，包含所有初始为 1 的位置坐标。
        3. 每次从队列中取出一个元素，检查其四个方向的邻居节点。
        4. 如果邻居是海洋（0），将其标记为陆地（1），并加入队列 Q。
        5. 更新距离 d，并将当前队列 q 替换为新队列 Q。
        6. 当所有位置都被访问后，返回最大距离 d。
        """
        n = len(grid)
        # 初始化队列 q，包含所有初始为 1 的位置坐标
        q = [[i, j] for i in range(n) for j in range(n) if grid[i][j]]
        
        d = -1
        # 当队列不为空且未访问完所有节点时
        while q and len(q) != n ** 2:
            Q = []
            for i, j in q:
                # 检查四个方向的邻居节点
                for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                        # 如果邻居是海洋，将其标记为陆地并加入队列 Q
                        grid[x][y] = 1
                        Q.append([x, y])
            q = Q
            d += 1
        
        return d

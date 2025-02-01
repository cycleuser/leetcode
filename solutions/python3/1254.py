
class Solution:
    # 定义深度优先搜索函数，检查封闭岛屿，并返回结果
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, ret=True):
            # 标记当前节点为已访问
            grid[i][j] = -1
            # 遍历四个方向的邻居节点
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n:
                    # 如果邻居节点为未访问，继续深度优先搜索
                    if not grid[x][y]:
                        ret &= dfs(x, y)
                else:
                    # 邻居节点越界，标记结果为False
                    ret = False
            return ret

        m, n = len(grid), len(grid[0])
        # 计算封闭岛屿的数量
        return sum(dfs(i, j) for i in range(m) for j in range(n) if grid[i][j] == 0)

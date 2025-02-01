
class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        """
        计算矩阵中不同岛屿的数量

        参数:
        - grid: 列表列表，表示网格地图。1 表示陆地，0 表示水域。

        返回值:
        不同形状的岛屿数量。
        """

        visited = set()  # 已访问的位置集合
        pattern = collections.defaultdict(str)  # 记录每块岛屿的形态
        m, n = len(grid), len(grid[0])  # 网格行数和列数

        def dfs(ri: int, rj: int, i: int, j: int, pi: int, pj: int) -> None:
            """
            深度优先搜索记录岛屿形状。

            参数:
            - ri, rj: 当前坐标相对起点的偏移量
            - i, j: 当前网格坐标
            - pi, pj: 相对于起点的位置变化量
            """
            visited.add((i, j))  # 标记当前位置已访问
            pattern[(ri, rj)] += str(pi) + str(pj)  # 记录当前位置相对起点的偏移

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + dx, j + dy  # 目标位置坐标
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] and (ni, nj) not in visited:
                    dfs(ri + dx, rj + dy, ni, nj, pi + dx, pj + dy)

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited:  # 未访问且为陆地
                    dfs(i, j, i, j, 0, 0)  # 开始深度优先搜索

        return len(set(pattern.values()))  # 返回不同岛屿形态的数量


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        :param grid: 一个二维数组，表示网格，0 表示可通过的格子，1 表示障碍物
        :return: 返回从左上角到右下角的最短路径长度，如果无解返回 -1
        """
        n = len(grid)
        # 起点为障碍物直接返回-1
        if grid[0][0] == 1:
            return -1
        
        bfs = [[0, 0]]  # 初始化bfs队列
        cnt = 1         # 记录路径长度
        seen = {(0, 0)} # 已访问集合

        while bfs:  # 当bfs队列不为空时循环
            new = []  # 新的一轮可扩展结点列表
            
            for i, j in bfs:
                for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1):
                    # 检查新结点的合法性
                    if 0 <= x < n and 0 <= y < n and (x, y) not in seen and not grid[x][y]:
                        # 如果到达终点，返回路径长度
                        if x == y == n - 1:
                            return cnt + 1
                        new.append((x, y))
                        seen.add((x, y))  # 记录已访问
                
            cnt += 1  # 更新步数
            bfs = new  # 移动bfs队列到下一轮的可扩展结点列表

        return -1  # 如果未找到路径，返回-1

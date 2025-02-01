
import heapq

class Solution:
    def findShortestWay(self, maze: list[list[int]], ball: list[int], hole: list[int]) -> str:
        """
        Find the shortest path from the ball to the hole in a 2D grid.
        
        参数:
            maze (list[list[int]]): 球所在的迷宫网格，0 表示空地，1 表示障碍物。
            ball (list[int]): 起始球的位置 [x, y]。
            hole (list[int]): 目标孔的位置 [x, y]。

        返回:
            str: 从起点到目标孔的最短路径表示字符串（例如 "ldu"），如果无解则返回 "impossible"。
        
        优化说明：
            - 使用优先队列来确保每次选择当前最小的距离进行扩展。
            - 借助哈希表记录已经访问过的节点及其路径长度和模式，避免重复计算。
        """
        m, n, q, stopped = len(maze), len(maze[0]), [(0, "", ball[0], ball[1])], {(ball[0], ball[1]): [0, ""]}
        
        while q:
            dist, pattern, x, y = heapq.heappop(q)
            
            # 如果球已经进入洞中
            if [x, y] == hole:
                return pattern
            
            for i, j, p in ((-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")):
                newX, newY, d = x, y, 0
                # 球继续滚动直到撞到障碍物或者边界
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                    
                    # 如果球已经进入洞中则直接退出循环
                    if [newX, newY] == hole: 
                        break
                
                # 只有当新位置未被访问过，或者找到了更短路径和模式时才继续
                if (newX, newY) not in stopped or [dist + d, pattern + p] < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = [dist + d, pattern + p]
                    heapq.heappush(q, (dist + d, pattern + p, newX, newY))
        
        return "impossible"

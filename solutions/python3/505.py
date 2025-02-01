
import heapq

class Solution:
    def shortestDistance(self, maze, start, destination):
        """
        中文注释: 该方法用于计算从起始点到目标点的最短距离。
        
        英文注释: This method is used to calculate the shortest distance from the start point to the destination.
        """
        m, n, q, stopped = len(maze), len(maze[0]), [(0, start[0], start[1])], {(start[0], start[1]): 0}
        
        # 使用优先队列进行最短路径搜索
        while q:
            dist, x, y = heapq.heappop(q)
            
            # 如果当前节点为目标点，直接返回距离
            if [x, y] == destination:
                return dist
            
            # 四个方向的移动
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newX, newY, d = x, y, 0
                
                # 移动直到遇到障碍物或超出边界
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                    
                # 如果新的位置没有被访问过，或者新计算的距离更短，则更新距离并加入优先队列
                if (newX, newY) not in stopped or dist + d < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = dist + d
                    heapq.heappush(q, (dist + d, newX, newY))
        
        # 如果没有到达目标点，返回 -1 表示无法到达
        return -1

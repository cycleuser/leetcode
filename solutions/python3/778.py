
class Solution:
    def swimInWater(self, grid):
        """
        Chinese:
        使用最小堆来解决游泳问题。从起点开始，每次选择当前高度最小且未访问过的格子。
        
        English:
        Solve the swimming problem using a minimum heap. Start from the origin and each time choose the unvisited cell with the smallest height.
        """
        import heapq
        # 初始化堆、结果变量、网格大小及已访问集合
        heap, res, n, visited = [(grid[0][0], 0, 0)], 0, len(grid), set()
        
        while True:
            d, i, j = heapq.heappop(heap)
            # 更新最大高度
            if d > res: 
                res = d
            
            # 判断是否到达终点
            if i == j == n - 1: 
                return res

            # 遍历相邻格子，加入堆中（未访问且在网格范围内）
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited: 
                    visited.add((x, y))
                    heapq.heappush(heap, (grid[x][y], x, y))


class Solution:
    def trapRainWater(self, heightMap):
        """
        计算给定高度地图中的雨水量

        :param heightMap: List[List[int]] 高度地图，二维数组表示地形的高度
        :return: int 返回可以存储的水量
        """

        m, n, heap, trapped = len(heightMap), len(heightMap and heightMap[0]), [], 0
        
        # 将外圈的格子加入堆中，并标记为已访问（-1）
        for i in range(m):
            for j in range(n):
                if i in {0, m - 1} or j in {0, n - 1}:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1
        
        # 处理堆中的每一个格子
        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                # 检查是否为内部格子且未访问
                if 0 < x < m - 1 and 0 < y < n - 1 and heightMap[x][y] != -1:
                    trapped += max(h - heightMap[x][y], 0)  # 计算并累加能存储的水量
                    heapq.heappush(heap, (max(heightMap[x][y], h), x, y))  # 将当前格子加入堆中
                    heightMap[x][y] = -1  # 标记为已访问
        
        return trapped

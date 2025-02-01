
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        """
        计算工人与自行车之间的最短距离。
        
        :param workers: 工人位置列表，每个元素表示一个工人的坐标 [x, y]
        :param bikes: 自行车位置列表，每个元素表示一辆自行车的坐标 [x, y]
        :return: 分配工人和自行车所需的最小成本
        """
        from heapq import heappush, heappop

        def dis(i, j):
            """计算工人i与自行车j之间的曼哈顿距离"""
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])

        h = [[0, 0, 0]]  # (成本, 工人索引, 自行车状态)
        seen = set()  # 记录已访问的状态
        while True:
            cost, i, taken = heappop(h)
            if (i, taken) in seen: 
                continue
            seen.add((i, taken))
            if i == len(workers):
                return cost
            for j in range(len(bikes)):
                if not taken & (1 << j):  # 检查自行车j是否已被分配
                    heappush(h, [cost + dis(i, j), i + 1, taken | (1 << j)])  # 更新状态并入堆

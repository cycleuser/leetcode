
class Solution:
    # 定义一个类来解决最小成本问题

    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # 初始化优先队列，起点城市成本为0
        heap = [(0, 1)]
        
        # 记录哪些城市已经被访问过
        visited = [0] * (N + 1)
        
        # 计算结果
        res = 0
        
        # 构建图结构
        graph = [[] for _ in range(N + 1)]
        for a, b, c in connections:
            graph[a].append([b, c])
            graph[b].append([a, c])

        # 使用优先队列进行遍历
        while heap:
            cost, city = heapq.heappop(heap)
            
            # 如果该城市已被访问，则跳过
            if visited[city]: 
                continue
            
            # 标记已访问的城市，并将成本累加到结果中
            visited[city] = 1
            res += cost
            
            # 将未访问的邻居城市和对应的成本加入优先队列
            for nCity, nCost in graph[city]:
                if not visited[nCity]:
                    heapq.heappush(heap, (nCost, nCity))
        
        # 检查所有城市是否都被访问过，返回结果或-1
        return res if all(visited[1:]) else -1

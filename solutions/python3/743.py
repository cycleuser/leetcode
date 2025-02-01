
class Solution:
    # 定义一个解决方案类

    def networkDelayTime(self, times, N, K):
        # 初始化队列，时间字典和邻接表
        q, t, adj = [(0, K)], {}, collections.defaultdict(list)
        
        # 构建邻接表
        for u, v, w in times:
            adj[u].append((v, w))
        
        # 使用优先队列进行Dijkstra算法
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time  # 记录当前节点最短时间
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))  # 更新邻接节点入队
        
        # 返回所有节点中最长的时间，即整个网络的延迟时间
        return max(t.values()) if len(t) == N else -1

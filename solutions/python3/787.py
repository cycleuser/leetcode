
class Solution:
    # 初始化航班信息字典，键为出发地，值为列表，包含目的地和价格元组
    def findCheapestPrice(self, n, flights, src, dst, K):
        from collections import defaultdict
        import heapq

        flight = defaultdict(list)
        for s, e, p in flights:
            flight[s].append((e, p))

        # 使用优先队列存储价格、城市和剩余中转次数，初始时为起点城市和K+1次中转机会的价格0
        heap = [(0, src, K + 1)]

        while heap:
            price, city, stop = heapq.heappop(heap)
            if city == dst:
                # 如果到达目的地，则返回当前价格
                return price
            elif stop > 0:
                # 对于每个邻居城市，更新剩余中转次数并加入优先队列
                for c, p in flight[city]:
                    heapq.heappush(heap, (price + p, c, stop - 1))

        # 如果未找到符合条件的路径，则返回-1
        return -1


class Solution:
    # 定义一个解决方案类

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 初始化优先队列
        heap = []

        # 遍历每个行程，按照上下车时间加入优先队列
        for a, b, c in trips:
            heapq.heappush(heap, (b, a))  # 上车站点入堆
            heapq.heappush(heap, (c, -a))  # 下车站点入堆（负数表示下车乘客）

        cur = 0  # 当前载客量

        # 遍历优先队列，处理每个事件
        while heap:
            time, passenger_change = heapq.heappop(heap)
            cur += passenger_change
            if cur > capacity: 
                return False  # 如果当前载客量超过容量限制，则返回False

        return True  # 所有行程结束后都没有超出载客量，返回True

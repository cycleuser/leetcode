
class HitCounter(object):

    # 初始化计数器，使用最小堆来存储时间戳
    def __init__(self):
        self.hits = []

    # 记录一次访问，并将时间戳加上300秒存入堆中
    def hit(self, timestamp):
        heapq.heappush(self.hits, timestamp + 300)

    # 获取过去300秒内的访问次数
    def getHits(self, timestamp):
        # 移除过期的时间戳（即小于当前时间减去300秒）
        while self.hits and self.hits[0] <= timestamp:
            heapq.heappop(self.hits)
        return len(self.hits)


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # 使用堆来优化合并操作，中英文注释
        heapq.heapify(sticks)  # 将列表转换为最小堆
        res = 0  # 记录代价

        # 当堆中还有两个或以上元素时循环
        while len(sticks) != 1:
            # 弹出两个最小的棍子
            new = heapq.heappop(sticks) + heapq.heappop(sticks)
            # 合并后的棍子加入堆中，并累加代价
            res += new
            heapq.heappush(sticks, new)

        return res  # 返回最终的合并代价

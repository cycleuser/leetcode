
class Solution:
    def minBuildTime(self, A: List[int], split: int) -> int:
        # 使用最小堆初始化工件列表 A
        heapq.heapify(A)
        
        # 当工件数量大于1时，不断进行合并操作
        while len(A) > 1:
            # 弹出两个最小的工件时间 x 和 y
            x, y = heapq.heappop(A), heapq.heappop(A)
            
            # 将新的工件时间 y + split 压入堆中
            heapq.heappush(A, y + split)
        
        # 最终返回剩余的单个工件的时间，即最小建造时间
        return heapq.heappop(A)

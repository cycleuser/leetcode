
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # 初始化堆、最小长度和当前累积和
        heap, l, sm = [], float("inf"), 0
        
        # 将初始值(0, -1)加入堆中，便于后续处理边界情况
        heapq.heappush(heap, (0, -1))
        
        # 遍历数组A中的每个元素
        for i, num in enumerate(A):
            sm += num  # 累加当前元素至累积和
            
            # 计算目标差值
            dif = sm - K
            
            # 检查堆顶元素是否满足条件，更新最小长度l
            while heap and (heap[0][0] <= dif or i - heap[0][1] >= l):
                preSum, preIndex = heapq.heappop(heap)
                if i - preIndex < l:
                    l = i - preIndex
            
            # 将当前累积和及其索引加入堆中
            heapq.heappush(heap, (sm, i))
        
        # 返回最小长度，若未找到满足条件的子数组，则返回-1
        return l if l != float("inf") else -1

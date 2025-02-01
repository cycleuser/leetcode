
class Solution:
    # 定义一个解决方案类，用于寻找第K小的质分数
    
    def kthSmallestPrimeFraction(self, A, K):
        # 使用最小堆来存储当前未访问的分母和分子对及其对应的值
        heap, used = [(A[0] / A[-1], 0, len(A) - 1)], {(0, len(A) - 1)}
        
        for i in range(K):
            try:
                # 弹出堆顶元素，并将其对应的分母和分子对添加到已访问集合中
                cur, l, r = heapq.heappop(heap)
                used.add((l, r))
                
                # 如果左侧的下一个分数组合未被访问过，那么就将它加入堆中并标记为已访问
                if (l + 1, r) not in used:
                    heapq.heappush(heap, (A[l + 1] / A[r], l + 1, r))
                    used.add((l + 1, r))
                
                # 如果右侧的上一个分数组合未被访问过，那么就将它加入堆中并标记为已访问
                if (l, r - 1) not in used:
                    heapq.heappush(heap, (A[l] / A[r - 1], l, r - 1))
                    used.add((l, r - 1))
            except:
                # 如果堆为空，则跳出循环，结束处理
                break
        
        # 返回第K小的质分数对应的分子和分母
        return [A[l], A[r]]

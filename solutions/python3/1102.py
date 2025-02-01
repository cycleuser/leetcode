
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        """
        使用最小堆来解决路径问题。
        
        1. 初始化一个最小堆，将起点（A[0][0]）的负值加入堆中。
        2. 取出堆顶元素，记录其数值并标记该位置为已访问。
        3. 更新结果变量res，取当前最小值。
        4. 若到达终点，则终止循环。
        5. 遍历当前位置的四个方向，将未访问且非负数的位置加入堆中。
        
        最终返回路径上的最小值res。
        """
        heap = [(-A[0][0], 0, 0)]
        res = A[0][0]
        m, n = len(A), len(A[0])
        while heap:
            val, i, j = heapq.heappop(heap)
            A[i][j] = -1
            res = min(res, -val)
            if i == m - 1 and j == n - 1:
                break
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n and A[x][y] >= 0:
                    heapq.heappush(heap, (-A[x][y], x, y))
        return res

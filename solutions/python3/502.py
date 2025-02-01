
class Solution:
    # 定义一个类来解决最大化投资资本的问题

    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        # 初始化可选项目池和当前可用项目的堆
        pool, new = [], [(c, p) for c, p in zip(Capital, Profits)]
        
        # 将当前可用的项目转换为最小堆
        heapq.heapify(new)
        
        # 执行k次投资操作
        for _ in range(k):
            # 优先选择可以立即开始的投资项目，即资本要求不大于当前资本W
            while new and new[0][0] <= W:
                c, p = heapq.heappop(new)
                heapq.heappush(pool, -p)  # 将利润加入到最大堆中（通过取负号）
            
            try:
                # 如果有可选项目，则执行投资项目
                p = -heapq.heappop(pool)
                W += p  # 更新当前资本W
            except:
                # 如果没有新的投资项目可供选择，退出循环
                break
        
        return W  # 返回最终的资本值

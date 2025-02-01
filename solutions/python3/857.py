
class Solution:
    # 初始化解决方案类

    def mincostToHireWorkers(self, quality, wage, K):
        """
        :param quality: 工人的质量列表，英文：List of workers' qualities
        :param wage: 工人的工资列表，英文：List of workers' wages
        :param K: 招聘的工人数量限制，英文：Limit on the number of hired workers
        :return: 最小成本，英文：Minimum cost to hire workers under given constraints
        """
        
        # 组合每个工人的质量与工资比值，并按此排序（升序）
        workers, res, heap, sumq = sorted((w / q, q, w) for q, w in zip(quality, wage)), float("inf"), [], 0
        
        # 遍历排序后的工人列表
        for ratio, q, w in workers:
            heapq.heappush(heap, -q)  # 将当前工人的质量加入堆中（取负以使用最小堆实现最大值）
            sumq += q  # 更新总质量
            
            if len(heap) > K:  # 如果堆中的工人数量超过K
                sumq += heapq.heappop(heap)  # 弹出一个质量最大的工人，减少总质量
                
            if len(heap) == K:  # 当堆中工人的数量等于K时
                res = min(res, ratio * sumq)  # 更新最小成本
        
        return res

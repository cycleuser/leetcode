
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        """
        初始化最小堆，以快速找到并处理最负的元素。
        
        参数:
            A (List[int]): 包含整数的列表
            K (int): 负数操作次数
        
        返回:
            int: 应用K次操作后的最大和
        """
        heapq.heapify(A)  # 将列表转换为最小堆，以便高效地获取最负元素
        
        for _ in range(K):
            val = heapq.heappop(A)  # 弹出并处理最负的元素
            heapq.heappush(A, -val)  # 推入其相反数
            
        return sum(A)  # 返回堆中所有元素之和，应用K次操作后


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        定义一个解决方案类，用于解决每日气温问题。
        
        参数:
            T (List[int]): 一维整数列表，表示每天的温度
        
        返回值:
            res (List[int]): 一维整数列表，表示等待升温天数
        """
        res = [0] * len(T)    # 初始化结果数组，长度与输入T相同，默认为0
        heap = []             # 初始化最小堆

        for j, t in enumerate(T):   # 遍历温度列表
            while heap and heap[0][0] < t:  # 当堆顶元素小于当前温度时进行弹出操作
                temp, i = heapq.heappop(heap)    # 弹出堆顶元素，并获取其索引和值
                res[i] = j - i   # 计算等待天数并存储在结果数组中

            heapq.heappush(heap, (t, j))  # 将当前温度及索引压入堆中
        
        return res    # 返回最终的结果数组

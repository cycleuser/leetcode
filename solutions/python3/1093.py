
from typing import List
import bisect

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        """
        计算统计量：最小值、最大值、均值、中位数和众数。

        参数：
            count (List[int]): 每个数值出现的次数列表

        返回：
            List[float]: 包含五个元素，分别为最小值、最大值、均值、中位数和众数
        """
        
        # 构造元组列表 [(索引, 出现次数)]
        arr = [(i, c * 1.0) for i, c in enumerate(count) if c]
        
        # 累积计数，用于后续计算均值、中位数
        acc = list(itertools.accumulate(count, lambda x, y: x + y))
        
        # 计算均值：加权平均值之和除以总次数
        mean = sum(i * c for i, c in arr) / acc[-1]
        
        # 众数是出现次数最多的数值，直接取最大
        mode = max(arr, key=lambda x: x[1])[0] * 1.0
        
        # 计算中位数：找到累积计数数组中两个中间位置的索引
        m1 = bisect.bisect(acc, (acc[-1] - 1) // 2)
        m2 = bisect.bisect(acc, acc[-1] // 2)
        
        # 返回五个统计量
        return [arr[0][0] * 1.0, arr[-1][0] * 1.0, mean, (m1 + m2) / 2.0, mode]

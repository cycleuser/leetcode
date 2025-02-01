
from collections import defaultdict
import bisect

class MajorityChecker:

    def __init__(self, arr: List[int]):
        """
        初始化数据结构，统计每个元素在数组中的位置，并按出现频率排序。
        
        Parameters:
            arr (List[int]): 输入的整数列表
        """
        self.dp = defaultdict(list)
        for i, v in enumerate(arr):
            self.dp[v].append(i)
        # 按出现频率从高到低排序
        self.occur = sorted([(len(v), k) for k, v in self.dp.items()], reverse=True)

    def query(self, left: int, right: int, threshold: int) -> int:
        """
        查询指定范围内出现次数超过阈值的多数元素。
        
        Parameters:
            left (int): 范围左边界
            right (int): 范围右边界
            threshold (int): 阈值

        Returns:
            int: 返回范围内的多数元素，如果不存在则返回-1
        """
        for o, v in self.occur:
            if o < threshold: break  # 如果当前元素出现次数小于阈值，则直接跳出循环
            l = self.dp[v]
            low = bisect.bisect_left(l, left)  # 查找左边界
            high = bisect.bisect_right(l, right)  # 查找右边界
            if high - low >= threshold:  # 判断范围内的元素数量是否满足阈值条件
                return v
        return -1

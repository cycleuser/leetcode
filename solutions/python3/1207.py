
from collections import Counter as cnt

# 定义解决方案类
class Solution:
    # 检查给定数组中每个元素出现的次数是否唯一
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 使用Counter统计arr中各数字的频率，再用Counter检查这些频率是否也唯一
        return all(v == 1 for v in cnt(cnt(arr).values()).values())

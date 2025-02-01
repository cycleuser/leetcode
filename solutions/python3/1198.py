
from itertools import chain as chn
from collections import Counter as cnt

class Solution:
    # 寻找最小的共同元素 - 中文注释：寻找矩阵中所有行的最小公共元素
    
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # 使用Counter统计所有元素出现次数 - 中文注释：使用计数器统计所有元素出现的频率
        counts = cnt(chn(*mat))
        
        # 找到出现次数等于矩阵行数的最小值 - 中文注释：找到出现次数等于矩阵行数的最小元素
        return min([k for k, v in counts.items() if v == len(mat)]) or -1  # 如果没有找到返回-1 - 英文注释: Return the smallest common element that appears in all rows, or -1 if no such element exists

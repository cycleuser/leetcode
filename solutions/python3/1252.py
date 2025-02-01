
from collections import Counter as cnt


class Solution:
    # 定义一个类来解决奇数格子问题
    
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # 计算在指定行和列中被修改的次数
        row = cnt(r for r, c in indices)  # 统计每一行被修改的次数
        col = cnt(c for r, c in indices)  # 统计每一列被修改的次数
        
        # 遍历所有可能的 (i,j) 对，计算奇数格子的数量
        return sum((row[i] + col[j]) % 2 for i in range(n) for j in range(m))

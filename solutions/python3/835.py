
class Solution:
    # 定义Solution类，用于解决两个矩阵的重叠问题

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        """
        :param A: 一个二进制矩阵（0 和 1）
        :param B: 另一个与A同大小的二进制矩阵
        :return: 返回两个矩阵重叠时最大1的数量
        
        通过计算所有可能的平移，找到使得A和B重叠后包含最多'1'的次数。
        """
        
        n = len(A)
        # 计算矩阵的大小

        shift_range = range(-n + 1, n)  # 平移范围从 - (n-1) 到 (n-1)

        max_overlap = 0
        for v in shift_range:
            for h in shift_range:
                overlap_count = sum(A[i][j] and B[i + v][j + h] 
                                    for i in range(n) for j in range(n) 
                                    if 0 <= i + v < n and 0 <= j + h < n)
                # 计算每个平移后A和B重叠的'1'的数量
                max_overlap = max(max_overlap, overlap_count)

        return max_overlap

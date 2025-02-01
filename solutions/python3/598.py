
class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        """
        :param m: 整数m，表示矩阵的行数
        :param n: 整数n，表示矩阵的列数
        :param ops: 列表，包含操作列表，每个操作为[行数, 列数]
        :return: 返回值是最大可能的小矩形个数
        """
        if not ops:
            # 如果没有操作，返回整个矩阵的大小
            return m * n
        
        min_row = min(op[0] for op in ops)  # 操作中的最小行数
        min_col = min(op[1] for op in ops)  # 操作中的最小列数

        # 最大可能的小矩形个数为：最小行数 * 最小列数
        return min_row * min_col

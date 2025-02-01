
class Solution:
    # 定义一个类，用于处理矩阵旋转操作

    def rotate(self, matrix):
        # 旋转90度的矩阵
        # 中文注释：此方法实现将输入的矩阵顺时针旋转90度
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]
        # 优化说明：使用切片操作`matrix[:]`来原地修改矩阵，避免额外的空间开销

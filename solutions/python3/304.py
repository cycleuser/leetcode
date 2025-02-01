
class NumMatrix:

    def __init__(self, matrix):
        # 初始化二维前缀和数组，大小比原矩阵大1
        # Chinese: 初始化一个二维前缀和数组 sums，其大小比输入的矩阵多一行一列。
        self.sums = [[0] * (len(matrix) and len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        
        # 遍历原矩阵填充前缀和数组
        # Chinese: 遍历输入的矩阵，计算并填充前缀和数组。
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.sums[i + 1][j + 1] = (self.sums[i][j + 1] +
                                           self.sums[i + 1][j] -
                                           self.sums[i][j] +
                                           matrix[i][j])

    def sumRegion(self, row1, col1, row2, col2):
        # 根据前缀和计算指定区域的和
        # Chinese: 使用前缀和数组快速求解给定矩形区域的元素总和。
        return self.sums[row2 + 1][col2 + 1] - self.sums[row2 + 1][col1] - self.sums[row1][col2 + 1] + self.sums[row1][col1]

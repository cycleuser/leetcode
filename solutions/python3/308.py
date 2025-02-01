
class NumMatrix(object):

    def __init__(self, matrix):
        """
        初始化数据结构。
        :type matrix: List[List[int]]
        """
        # 前缀和优化，累加每一行的前一个元素
        for row in matrix:
            for col in range(1, len(row)):
                row[col] += row[col-1]
        self.matrix = matrix

    def update(self, row, col, val):
        """
        更新矩阵[row,col]位置的值为val。
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        # 计算原值与差值
        original = self.matrix[row][col]
        if col != 0:
            original -= self.matrix[row][col-1]

        diff = original - val

        for y in range(col, len(self.matrix[0])):
            self.matrix[row][y] -= diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        计算矩阵中[(row1,col1)..(row2,col2)]范围内元素的和。
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # 计算指定区域的和
        sum = 0
        for x in range(row1, row2 + 1):
            sum += self.matrix[x][col2]
            if col1 != 0:
                sum -= self.matrix[x][col1 - 1]
        return sum

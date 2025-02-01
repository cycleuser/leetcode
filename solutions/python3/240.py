
class Solution:
    # 检查二维矩阵中是否包含目标值

    def searchMatrix(self, matrix, target):
        # 使用任何一行中存在目标值来判断整个矩阵是否包含目标值
        return any(target in row for row in matrix)



class Solution:
    # Check if the target value is present in the given 2D matrix.

    def searchMatrix(self, matrix, target):
        # Use any() to check if there exists a row that contains the target.
        return any(target in row for row in matrix)

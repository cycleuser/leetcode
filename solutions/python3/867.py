
class Solution:
    # 定义一个方法transpose，传入参数A
    def transpose(self, A):
        # 使用列表推导式实现矩阵转置
        # 中文注释：使用列表推导式进行矩阵转置操作。遍历外层j范围为A[0]的长度（列数），内层i范围为A的长度（行数）。
        # 英文注释: Use list comprehension to transpose the matrix. Outer loop j ranges over the length of A[0] (number of columns), inner loop i ranges over the length of A (number of rows).
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

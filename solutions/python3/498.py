
class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :param matrix: List[List[int]] - 输入的矩阵
        :return: List[int] - 矩阵对角线遍历的结果
        
        思路：使用双指针模拟对角线遍历过程。定义方向变量 d 来控制移动方向。
        """
        i, j, d, res, n, m = 0, 0, 1, [], len(matrix), len(matrix[0]) if matrix else 0
        while i < n and j < m:
            res.append(matrix[i][j])
            # 判断是否到达边界或方向改变点，调整指针和方向
            if j + 1 < m and (i == 0 and d == 1) or (i == n - 1 and d == -1): 
                j, d = j + 1, -d
            elif i + 1 < n and (j == 0 and d == -1) or (j == m - 1 and d == 1):
                i, d = i + 1, -d
            # 继续按当前方向移动指针
            elif d == 1: 
                i, j = i - 1, j + 1
            else: 
                i, j = i + 1, j - 1
        return res

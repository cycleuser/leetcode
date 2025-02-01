
class Solution:
    # 解决矩阵置零问题，将值为0的元素所在行和列全部置为0
    def setZeroes(self, matrix):
        m, n, x = len(matrix), len(matrix[0] if matrix else []), 0

        # 向下传播0的影响
        for i in range(m - 1):
            for j in range(n):
                if not matrix[i][j] and matrix[i + 1][j]:
                    matrix[i + 1][j] = None
        
        # 向上传播0的影响
        for i in range(m - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                if not matrix[i][j] and matrix[i + 1][j]:
                    matrix[i][j] = None

        # 确定0的具体位置并置零
        while x < m:
            y = 0
            while y < n:
                if matrix[x][y] == 0: 
                    matrix[x] = [0] * n
                elif not matrix[x][y]: 
                    matrix[x][y] = 0
                y += 1 
            x += 1

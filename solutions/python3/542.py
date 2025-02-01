
class Solution:
    # 定义一个类来解决更新矩阵的问题

    def updateMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        # 获取矩阵的行数和列数
        m, n = len(matrix), len(matrix[0])
        
        # 第一遍遍历，将所有非零元素初始化为无穷大，并检查其上方或左方的邻居元素是否可以减少距离
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float("inf")
                    # 检查上方元素，如果上方元素+1更小，则更新当前元素的距离
                    if i > 0 and matrix[i - 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i - 1][j] + 1
                    # 检查左方元素，如果左方元素+1更小，则更新当前元素的距离
                    if j > 0 and matrix[i][j - 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j - 1] + 1

        # 第二遍遍历，检查下方或右方的邻居元素是否可以减少距离，并进行更新
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    # 检查下方元素，如果下方元素+1更小，则更新当前元素的距离
                    if i + 1 < m and matrix[i + 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i + 1][j] + 1
                    # 检查右方元素，如果右方元素+1更小，则更新当前元素的距离
                    if j + 1 < n and matrix[i][j + 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j + 1] + 1

        return matrix

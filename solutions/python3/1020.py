
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        """
        计算矩阵中的封闭岛屿数量。封闭岛屿指的是所有值为1且不与边界相连的区域。
        
        :param A: List[List[int]] - 输入的二维矩阵，其中0表示水域，1表示陆地
        :return: int - 封闭岛屿的数量
        """
        
        def dfs(i, j):
            """
            深度优先搜索函数，用于标记访问过的陆地标记为0，并递归访问其相邻的陆地。
            
            :param i: int - 当前行索引
            :param j: int - 当前列索引
            """
            A[i][j] = 0  # 将当前陆地标记为已访问（水域）
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and A[x][y]:
                    dfs(x, y)  # 访问相邻陆地
        
        m, n = len(A), len(A[0])  # 获取矩阵的行数和列数
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j)  # 从边界上的陆地开始进行深度优先搜索
        
        return sum(sum(row) for row in A)  # 计算剩余的1的数量，即封闭岛屿的数量

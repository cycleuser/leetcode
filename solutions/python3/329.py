
class Solution:
    # 定义解决方案类

    def longestIncreasingPath(self, matrix):
        # 计算给定矩阵中的最长递增路径长度
        
        def dfs(i, j):
            # 深度优先搜索，计算从(i,j)位置开始的最长递增路径长度
            if not dp[i][j]:
                # 如果dp[i][j]未被初始化，则进行计算
                dp[i][j] = 1 + max(
                    (dfs(x, y) for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)) 
                     if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]), 
                    default=0
                )
            return dp[i][j]
        # 初始化矩阵的行数m和列数n
        m, n = len(matrix), len(matrix[0])
        # 初始化dp数组，用于存储每个位置的最大递增路径长度
        dp = [[0] * n for _ in range(m)]
        # 返回整个矩阵中所有起点的最长递增路径中的最大值
        return max((dfs(i, j) for i in range(m) for j in range(n)), default=0)

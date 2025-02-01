
class Solution:
    # 游戏生命函数
    def gameOfLife(self, board: List[List[int]]) -> None:
        # 获取矩阵的行数和列数
        m, n = len(board), len(board[0])
        
        # 创建一个新的矩阵用于存储新的状态
        matrix = [[0] * n for _ in range(m)]
        
        # 遍历原矩阵中的每个元素
        for i in range(m):
            for j in range(n):
                cnt = 0
                
                # 计算当前元素周围的存活细胞数量
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1),
                             (i - 1, j - 1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1)):
                    if 0 <= x < m and 0 <= y < n and board[x][y] == 1:
                        cnt += 1
                
                # 根据规则更新新矩阵中的状态
                if (board[i][j] and 2 <= cnt <= 3) or (not board[i][j] and cnt == 3):
                    matrix[i][j] = 1
        
        # 将原矩阵的状态更新为新的状态
        for i in range(m):
            for j in range(n):
                board[i][j] = matrix[i][j]

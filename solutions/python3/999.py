
class Solution:
    # 初始化解决方案类

    def numRookCaptures(self, board: List[List[str]], res = 0) -> int:
        # 计算棋盘中皇后能吃掉的子的数量
        
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    # 找到第一个R（皇后）的位置
                    
                    # 检查向上是否有可吃的棋子
                    for x in range(i - 1, -1, -1):
                        if board[x][j] in 'Bp':
                            res += board[x][j] == 'p'
                            break
                    # 检查向下是否有可吃的棋子
                    for x in range(i + 1, 8):
                        if board[x][j] in 'Bp':
                            res += board[x][j] == 'p'
                            break
                    # 检查向左是否有可吃的棋子
                    for y in range(j - 1, -1, -1):
                        if board[i][y] in 'Bp':
                            res += board[i][y] == 'p'
                            break
                    # 检查向右是否有可吃的棋子
                    for y in range(j + 1, 8):
                        if board[i][y] in 'Bp':
                            res += board[i][y] == 'p'
                            break
        return res  # 返回总数

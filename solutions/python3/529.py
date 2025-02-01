
class Solution(object):
    def updateBoard(self, board, click):
        """
        :param board: List[List[str]] - 代表游戏板的状态，其中'M'表示地雷，'B'表示空白，数字表示周围地雷数量。
        :param click: List[int] - 点击的位置 (i, j)。
        :return: List[List[str]] - 更新后的游戏板状态。
        """
        
        def explore(i, j):
            """
            深度优先搜索函数，用于探索并标记相邻的空白格子或地雷数量。
            
            :param i: int - 当前行索引
            :param j: int - 当前列索引
            """
            visited.add((i, j))
            if board[i][j] == "M":
                # 如果是地雷，则标记为X
                board[i][j] = "X"
            else:
                points = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j + 1), (i + 1, j - 1)]
                cnt, adj = 0, []
                
                for p in points:
                    if 0 <= p[0] < m and 0 <= p[1] < n:  # 检查点是否在边界内
                        if board[p[0]][p[1]] == "M": 
                            cnt += 1
                        elif p not in visited: 
                            adj.append(p)
                
                if cnt == 0:
                    # 如果没有相邻地雷，则标记为B并继续探索
                    board[i][j] = "B"
                    for p in adj: explore(p[0], p[1])
                else:
                    # 否则，记录周围地雷数量
                    board[i][j] = str(cnt)
        
        m, n, visited = len(board), len(board and board[0]), set()  # 获取行数、列数和已访问集合
        explore(click[0], click[1])  # 从点击位置开始探索
        return board  # 返回更新后的游戏板状态

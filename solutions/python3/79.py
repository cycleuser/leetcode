
class Solution:
    def exist(self, board, word):
        """
        判断是否可以在棋盘中找到给定单词。
        
        :param board: 二维列表，表示游戏棋盘
        :param word: 字符串，要查找的单词
        """
        m, n, o = len(board), len(board and board[0]), len(word)
        
        def explore(i, j, k, q):
            """
            深度优先搜索辅助函数
            
            :param i: 当前行索引
            :param j: 当前列索引
            :param k: 当前单词索引
            :param q: 已访问过的坐标集合
            """
            for x, y in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)):
                if k >= o or (0 <= x < m and 0 <= y < n and board[x][y] == word[k]
                              and (x, y) not in q and explore(x, y, k + 1, q | {(x, y)})):
                    return True
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and explore(i, j, 1, {(i, j)}):
                    return True
        return False


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        解题思路：首先标记所有边缘的'O'和与其相连的'O'为'S'(Safe)，然后将剩余的所有'O'置为'X'，最后将所有的'S'还原为'O'
        """

        m, n = len(board), len(board and board[0])

        """
        辅助函数，深度优先搜索并标记所有与边界'O'相连的'O'
        """
        def explore(i: int, j: int) -> None:
            board[i][j] = "S"
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                    explore(x, y)

        """
        遍历四个边界，将所有'O'及其相连的'O'标记为'S'
        """
        for i in range(max(m, n)):
            if i < m and board[i][0] == "O":
                explore(i, 0)
            if i < m and board[i][n - 1] == "O":
                explore(i, n - 1)
            if i < n and board[0][i] == "O":
                explore(0, i)
            if i < n and board[m - 1][i] == "O":
                explore(m - 1, i)

        """
        将所有剩余的'O'标记为'X'
        """
        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

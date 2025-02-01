class Solution:
    def solveNQueens(self, n: int) -> list[str]:
        """
        解决N皇后问题，返回所有满足条件的棋盘布局。
        
        参数:
            n (int): 棋盘大小（n x n）
            
        返回:
            list[str]: 所有解决方案的字符串表示
        """
        result = []

        def dfs(i: int, left_diag: int, right_diag: int, col: int, board: list[str]):
            if i == n:
                result.append(board[:])
                return
            
            for j in range(n):
                if (col & (1 << j)) and \
                   (left_diag & (1 << (i + j))) and \
                   (right_diag & (1 << (n - 1 + i - j))):
                    # Place queen and mark positions as unavailable
                    col ^= (1 << j)
                    left_diag ^= (1 << (i + j))
                    right_diag ^= (1 << (n - 1 + i - j))
                    
                    new_row = "." * j + "Q" + "." * (n - j - 1)
                    dfs(i + 1, left_diag, right_diag, col, board + [new_row])
                    
                    # Backtrack
                    col ^= (1 << j)
                    left_diag ^= (1 << (i + j))
                    right_diag ^= (1 << (n - 1 + i - j))

        # Initialize with all positions available
        dfs(0, (1 << (2*n)) - 1, (1 << (2*n)) - 1, (1 << n) - 1, [])
        return result
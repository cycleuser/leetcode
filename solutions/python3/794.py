
class Solution(object):
    def check_win_positions(self, board, player):
        """
        检查给定玩家是否有胜利位置。
        如果有胜利位置返回True，否则返回False。
        """
        # 检查行
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True

        # 检查列
        for i in range(len(board)):
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True

        # 检查对角线
        if (board[0][0] == board[1][1] == board[2][2] == player or 
            board[0][2] == board[1][1] == board[2][0] == player):
            return True

        return False
    
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        
        x_count, o_count = 0, 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    x_count += 1
                elif board[i][j] == "O":
                    o_count += 1

        # 检查棋子数量是否合理
        if o_count > x_count or x_count - o_count > 1:
            return False

        # 检查胜利条件是否合理
        if self.check_win_positions(board, 'O'):
            if self.check_win_positions(board, 'X'):
                return False
            return o_count == x_count
        
        if self.check_win_positions(board, 'X') and x_count != o_count + 1:
            return False

        return True

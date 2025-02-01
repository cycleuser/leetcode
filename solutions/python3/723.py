
class Solution:
    def candyCrush(self, board):
        """
        解决糖果粉碎问题的类方法

        :param board: 游戏棋盘，二维列表表示
        :return: 经过一系列操作后的最终状态的棋盘
        """

        m, n = len(board), len(board[0])
        
        def gravity():
            """
            重力作用：将每列中零元素填充到下部空位

            遍历每一列，从底部开始取非零值，并将其存入栈。再从顶部开始填充值至该列。
            """
            for j in range(n):
                stack = [board[i][j] for i in range(m - 1, -1, -1) if board[i][j] > 0]
                stack += [0] * (m - len(stack))
                for i in range(m): 
                    board[i][j] = stack.pop()
        
        def crush():
            """
            粉碎操作：检查并标记可以粉碎的糖果

            遍历每一行和列，寻找连续相等绝对值的三个糖果进行标记。
            如果有多个位置被标记，则返回True表示需要执行一次gravity()操作；否则返回False表示无需进一步操作。
            """
            crush = False
            for i in range(m):
                for j in range(n):
                    # 检查水平方向是否有连续相等的三个糖果
                    if j > 1 and board[i][j] > 0 and abs(board[i][j]) == abs(board[i][j - 1]) == abs(board[i][j - 2]):
                        board[i][j - 2:j + 1] = [-abs(board[i][j]) for _ in range(3)]
                        crush = True
                    # 检查垂直方向是否有连续相等的三个糖果
                    if i > 1 and abs(board[i][j]) != 0 and abs(board[i][j]) == abs(board[i - 1][j]) == abs(board[i - 2][j]):
                        board[i][j] *= -1  # 粉碎当前及下方两行的正数糖果
                        if j > 0: 
                            board[i - 1][j] *= -1  # 同上，处理右侧相邻列
                            if i > 0: 
                                board[i - 2][j] *= -1  # 同上，处理左侧相邻列
                        crush = True
            return crush

        while crush():
            gravity()
        
        return board

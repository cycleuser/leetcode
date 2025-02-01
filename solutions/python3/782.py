
class Solution:
    def movesToChessboard(self, b):
        """
        :param b: List[List[int]] - 棋盘状态，0表示空位，1表示棋子
        :return: int - 将棋盘变为标准国际象棋排列所需的最少移动次数，-1表示无法完成
        
        1. 首先检查每行和每列的初始状态是否满足要求。
           中文：首先检查每一行和每一列的初始状态是否满足要求。
        """
        N = len(b)
        
        # 检查对角线元素，确保不冲突
        if any(b[0][0] ^ b[i][0] ^ b[0][j] ^ b[i][j] for i in range(N) for j in range(N)):
            return -1
        
        # 检查每行和每列棋子数量是否满足要求，不超过总数的一半
        if not N // 2 <= sum(b[0]) <= (N + 1) // 2:
            return -1
        if not N // 2 <= sum(b[i][0] for i in range(N)) <= (N + 1) // 2:
            return -1
        
        # 统计第0行和第0列满足标准排列的元素个数
        col = sum(b[0][i] == i % 2 for i in range(N))
        row = sum(b[i][0] == i % 2 for i in range(N))
        
        # 如果棋盘大小为奇数，调整col和row使其满足标准排列的条件
        if N % 2:
            if col % 2:
                col = N - col
            if row % 2:
                row = N - row
        else:  # 棋盘大小为偶数时的情况
            col = min(N - col, col)
            row = min(N - row, row)
        
        return (col + row) // 2

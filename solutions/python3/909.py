
class Solution:
    def snakesAndLadders(self, board):
        """
        定义一个方法，接收棋盘列表board作为输入。
        
        :param board: 棋盘的二维数组表示
        :return: 返回从起点到终点所需的最少移动次数，若无法到达则返回-1
        """
        # 初始化辅助数组、棋盘大小、队列、已访问标记集和步数计数器
        arr, nn, q, seen, moves = [0], len(board) ** 2, [1], set(), 0
        
        # 将board中的行反向并按奇偶调整顺序添加至arr中，构建从终点到起点的线性表示
        for i, row in enumerate(board[::-1]):
            arr += row[::-1] if i % 2 else row

        # 使用广度优先搜索遍历棋盘上的所有可能路径
        while q:
            new = []
            for sq in q:
                if sq == nn: return moves 
                for i in range(1, 7):
                    # 计算下一步位置，检查是否已访问过，并更新队列和步数计数器
                    if sq + i <= nn and sq + i not in seen:
                        seen.add(sq + i)
                        new.append(sq + i if arr[sq + i] == -1 else arr[sq + i])
            q, moves = new, moves + 1
        
        return -1 

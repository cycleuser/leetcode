
class TicTacToe:

    def __init__(self, n: int):
        """
        初始化游戏，设定棋盘大小n，并初始化行、列计数器和对角线计数器。
        
        :param n: 棋盘的大小
        """
        self.n = n
        # 使用defaultdict存储每行和每列的得分情况
        self.rows, self.cols = collections.defaultdict(int), collections.defaultdict(int)
        # 初始化两个对角线的计数器
        self.d = 0
        self.ad = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        执行玩家在指定位置下的棋子，并判断是否有人获胜。

        :param row: 棋子所在的行
        :param col: 棋子所在的列
        :param player: 玩家标识（1或2）
        :return: 返回获胜的玩家编号，若无玩家获胜则返回0
        """
        add = 1 if player == 1 else -1

        # 更新行和列对应的得分情况
        self.rows[row] += add
        self.cols[col] += add

        # 检查是否在主对角线或副对角线上
        if row == col:
            self.d += add
        if row == self.n - col - 1:
            self.ad += add

        # 判断当前操作后是否有人获胜
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.d) == self.n or abs(self.ad) == self.n:
            return player
        elif self.rows[row] == -self.n or self.cols[col] == -self.n or self.d == -self.n or self.ad == -self.n:
            return 3 - player  # 如果是玩家2获胜，返回1；如果是玩家1获胜，则返回2
        else:
            return 0


class Solution:
    def countBattleships(self, board):
        """
        计算海图上战舰的数量。

        通过遍历二维数组，判断每个 "X" 是否代表一艘完整的战舰。
        
        :param board: List[List[str]] - 海图的表示形式，'.' 表示水，'X' 表示战舰的一部分
        :return: int - 战舰的数量
        """
        # 使用生成器表达式来计算战舰数量，优化性能并减少内存使用
        return sum(
            board[i][j] == "X"  # 当前位置是 "X"
            and (i == 0 or board[i-1][j] == ".")  # 上方不是 "X"
            and (j == 0 or board[i][j-1] == ".")  # 左侧不是 "X"
            for i in range(len(board))  # 遍历行
            for j in range(len(board[0]))  # 遍历列
        )

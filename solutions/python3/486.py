
class Solution:
    def PredictTheWinner(self, nums):
        """
        判断当前玩家是否能赢得游戏。使用深度优先搜索（DFS）来模拟游戏过程。

        :param nums: List[int] - 游戏中可选的数字列表
        :return: bool - 当前玩家是否有足够的策略确保胜利
        """

        def dfs(l, r, p1, p2, turn):
            """
            使用深度优先搜索递归模拟游戏。

            :param l: int - 数组左边界索引
            :param r: int - 数组右边界索引
            :param p1: int - 玩家1当前得分
            :param p2: int - 玩家2当前得分
            :param turn: bool - 当前是否为玩家1的回合（True表示是）
            :return: bool - 如果当前玩家能赢得游戏则返回True，否则False
            """
            if l > r:
                # 边界条件：如果索引越界，则比赛结束，检查得分
                return p1 >= p2
            elif turn:
                # 玩家1的回合
                # 选择左边或右边的数字，并递归调用以判断是否能获胜
                return dfs(l + 1, r, p1 + nums[l], p2, 0) or dfs(l, r - 1, p1 + nums[r], p2, 0)
            else:
                # 玩家2的回合
                # 必须选择左边或右边的数字，且确保玩家1不能获胜
                return dfs(l + 1, r, p1, p2 + nums[l], 1) and dfs(l, r - 1, p1, p2 + nums[r], 1)

        # 游戏开始时调用DFS函数，假设当前为玩家1的回合
        return dfs(0, len(nums) - 1, 0, 0, 1)

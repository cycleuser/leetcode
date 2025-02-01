
import collections

class Leaderboard:

    # 初始化 leaderboard，使用 defaultdict 来存储玩家分数和对应的 player ID 集合
    def __init__(self):
        self.scores = collections.defaultdict(set)  # 存储分数及其对应 players 的集合
        self.p = collections.defaultdict(int)       # 存储每个玩家的当前分数

    # 添加分数，更新玩家的分数，并在适当的位置插入新的分数
    def addScore(self, playerId: int, score: int) -> None:
        current_score = self.p[playerId]  # 获取当前分数
        self.scores[current_score].discard(playerId)  # 从旧分数集合中移除玩家ID
        self.p[playerId] += score              # 更新玩家的分数
        self.scores[self.p[playerId]].add(playerId)  # 将玩家加入新分数对应的集合

    # 返回前 K 名玩家的总分，按分数降序排列
    def top(self, K: int) -> int:
        sm = cnt = 0
        for score, players in sorted(self.scores.items())[::-1]:  # 按分数降序遍历 scores
            if len(players) + cnt <= K:                             # 如果当前玩家数量加上累计数量小于等于K
                sm += len(players) * score                           # 累加总分
                cnt += len(players)                                 # 更新累计计数
            else:
                sm += (K - cnt) * score                              # 计算剩余部分的分数并累加
                cnt = K                                               # 累计数量达到K，退出循环
        return sm

    # 重置玩家分数为0，并将其加入到分数为0的集合中
    def reset(self, playerId: int) -> None:
        current_score = self.p[playerId]  # 获取当前分数
        self.scores[current_score].discard(playerId)  # 从旧分数集合中移除玩家ID
        self.p[playerId] = 0                    # 重置玩家分数为0
        self.scores[0].add(playerId)            # 将玩家加入到分数为0的集合


class TopVotedCandidate:

    # 初始化类，记录投票结果和获胜者
    def __init__(self, persons, times):
        import collections
        
        votes = collections.defaultdict(int)
        winner = 0
        self.winners = [None] * len(times)
        self.times = times

        for i, person in enumerate(persons):
            votes[person] += 1
            if votes[person] >= votes[winner]:
                winner = person
            self.winners[i] = winner

    # 查询给定时刻的获胜者
    def q(self, t):
        import bisect
        
        return self.winners[bisect.bisect(self.times, t) - 1]

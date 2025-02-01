
class Solution:
    # 定义一个类来解决修改数组的问题

    def getModifiedArray(self, length: int, updates: list[tuple[int, int, int]]) -> list[int]:
        # 初始化起始位置、结束位置的增量字典和结果数组
        start, end, res, cur = collections.defaultdict(int), collections.defaultdict(int), [0] * length, 0

        # 遍历所有更新操作，记录每个位置的增量变化
        for s, e, inc in updates:
            start[s] += inc
            end[e] += -inc

        # 计算实际数组值的变化
        for i in range(length):
            if start[i]:
                cur += start[i]
            res[i] += cur
            if end[i]:
                cur += end[i]

        return res  # 返回修改后的数组



class Solution:
    def getModifiedArray(self, length: int, updates: list[tuple[int, int, int]]) -> list[int]:
        start, end, res, cur = collections.defaultdict(int), collections.defaultdict(int), [0] * length, 0

        for s, e, inc in updates:
            start[s] += inc
            end[e] += -inc

        for i in range(length):
            if start[i]:
                cur += start[i]
            res[i] += cur
            if end[i]:
                cur += end[i]

        return res

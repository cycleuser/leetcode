
class Solution:
    """
    Solution 类，包含 countTriplets 方法用于计算满足特定条件的三元组数量。
    """

    def countTriplets(self, A: List[int]) -> int:
        # 使用 Counter 统计所有可能的按位与结果及其出现次数
        cnt = collections.Counter([a & b for a in A for b in A])

        # 计算满足条件的三元组数量：对于每个元素 a 和统计中所有 k，如果 a 与 k 的按位与结果为 0，则累加计数
        return sum(cnt[k] for a in A for k in cnt if not a & k)


class Solution:
    def numSubarraysWithSum(self, A: list[int], S: int) -> int:
        """
        计算数组中和为S的连续子数组的数量。

        参数:
        A (list[int]): 输入整数列表。
        S (int): 目标和。

        返回值:
        int: 和为S的连续子数组数量。
        """

        res, sm, sums = 0, 0, collections.defaultdict(int)
        # 初始化结果计数器res、当前累积和sm以及使用字典存储累积和出现次数
        for a in A:
            sm += a
            # 每次累加当前元素a到累积和sm中
            res += sums[sm - S] + (sm == S)
            # 如果当前累积和等于目标S，直接计数；否则查找差值在字典中的出现次数并累计结果
            sums[sm] += 1
            # 将当前累积和的出现次数加一记录到字典中
        return res
        # 返回最终的结果计数器res

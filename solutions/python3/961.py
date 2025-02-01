
class Solution:
    # 定义一个类来解决重复N次的元素问题

    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 使用collections.Counter计算列表中每个元素出现的次数
        # 返回出现次数最多的那个元素，由于题目保证了一定存在一个重复的元素，
        # 所以most_common(1)返回的是一个包含单个元组的列表，[0][0]取出这个元组的第一个值
        return collections.Counter(A).most_common(1)[0][0]

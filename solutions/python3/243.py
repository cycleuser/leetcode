
class Solution:
    # 定义一个类来解决最短距离问题

    def shortestDistance(self, words, word1, word2):
        # 初始化索引和最小距离变量
        i1, i2, mn = -1, -1, float("inf")

        # 遍历单词列表，获取两个指定单词的最近距离
        for i, w in enumerate(words):
            if w == word1:
                i1 = i  # 记录word1的索引
                if i2 >= 0:  # 如果之前已经记录过word2的索引，则计算当前最短距离
                    mn = min(mn, i - i2)
            elif w == word2:
                i2 = i  # 记录word2的索引
                if i1 >= 0:  # 如果之前已经记录过word1的索引，则计算当前最短距离
                    mn = min(mn, i - i1)

        return mn  # 返回找到的最短距离

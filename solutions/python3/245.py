
class Solution:
    # 定义一个类来解决最短距离问题

    def shortestWordDistance(self, words, word1, word2):
        # 初始化索引和结果变量
        i1 = i2 = -1
        res, same = float("inf"), word1 == word2
        
        # 遍历每个单词及其对应的索引
        for i, w in enumerate(words):
            if w == word1:
                # 如果是相同的词，更新第二个词的索引为第一个词的旧索引
                if same: 
                    i2 = i1
                # 更新第一个词的新索引
                i1 = i
                # 如果两个词的索引都有值了，计算距离并更新结果变量
                if i2 >= 0: 
                    res = min(res, abs(i1 - i2))
            elif w == word2:
                # 更新第二个词的新索引
                i2 = i
                # 如果第一个词有索引了，计算距离并更新结果变量
                if i1 >= 0: 
                    res = min(res, abs(i2 - i1))
        
        return res  # 返回最短距离

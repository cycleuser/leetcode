
class Solution:
    # 定义一个类来解决寻找词频前k高的问题

    def topKFrequent(self, words, k):
        # 返回词频前k高且字典序较小的单词列表
        
        # 使用collections.Counter计算每个单词的频率
        return [w for w, v in sorted(collections.Counter(words).items(), key=lambda x: (-x[1], x[0]))[:k]]
        # 通过sorted对Counter的结果进行排序，并取前k个元素

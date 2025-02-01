
class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        """
        判断两个句子是否相似。如果一个词组与另一个词组相同或者在给定的词对中出现，则认为两个句子相似。
        
        参数：
            - words1: 第一个句子，由多个单词组成
            - words2: 第二个句子，由多个单词组成
            - pairs: 词对列表，表示可互换的词语
        
        返回值：
            如果两个句子相似则返回 True，否则返回 False
        """
        
        # 使用字典存储每个词出现的所有相似词（双向关系）
        sim = collections.defaultdict(set)
        for a, b in pairs:
            sim[a].add(b)  # 将a添加到b的相似词集合中
            sim[b].add(a)  # 将b添加到a的相似词集合中
        
        # 检查两个句子长度是否相同，且每个单词对是否满足相似条件
        return len(words1) == len(words2) and all(w1 == w2 or w2 in sim[w1] for w1, w2 in zip(words1, words2))

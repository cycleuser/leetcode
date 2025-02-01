
class Solution:
    # 定义一个方法来计算每个单词的最小字符频率
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # 对words列表中的每个字符串，找到其中出现次数最多的最小字符，并将这些值排序后存储到f中
        f = sorted(w.count(min(w)) for w in words)
        
        # 遍历queries列表中的每个查询字符串q，计算其最小频率，并返回比它大的f的元素个数
        return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]

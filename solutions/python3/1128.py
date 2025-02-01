
class Solution:
    # 定义一个方法来计算等价的多米诺骨牌对数

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 使用collections.Counter统计每个排序后的多米诺骨牌出现次数
        from collections import Counter
        
        # 对每一个多米诺骨牌进行排序，并转化为元组形式便于计数
        count = Counter(tuple(sorted(d)) for d in dominoes)
        
        # 计算等价的多米诺骨牌对数：v * (v - 1) // 2 是组合数学中的计算公式，用于计算v个元素两两组合的数量
        return sum(v * (v - 1) // 2 for v in count.values())

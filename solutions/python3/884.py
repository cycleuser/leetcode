
class Solution:
    # 定义一个类来解决问题

    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        # 使用collections.Counter统计单词出现次数
        c1 = collections.Counter(A.split())
        c2 = collections.Counter(B.split())
        
        # 找出只在A中出现一次且不在B中的单词
        uncommon_in_A = [c for c in c1 if c1[c] == 1 and c not in c2]
        
        # 找出只在B中出现一次且不在A中的单词
        uncommon_in_B = [c for c in c2 if c2[c] == 1 and c not in c1]
        
        # 返回所有不常见的单词
        return uncommon_in_A + uncommon_in_B

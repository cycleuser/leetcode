
class Solution:
    # 这个方法用于统计字符串 S 中作为宝石的字符数量，这些字符在字符串 J 中被定义为宝石
    def numJewelsInStones(self, J: str, S: str) -> int:
        # 将字符串 J 转换为集合 sj 以提高查找效率
        sj = set(J)
        
        # 使用生成器表达式遍历字符串 S，对于每个字符 s，检查其是否在集合 sj 中，并求和统计
        return sum(s in sj for s in S)

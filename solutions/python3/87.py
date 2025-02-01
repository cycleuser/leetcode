
class Solution:
    # 判断字符串s1和s2是否为搅乱字符串（Scramble String）
    
    def isScramble(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        # 如果长度不等或排序后不同，则不是搅乱字符串
        if n != m or sorted(s1) != sorted(s2):
            return False
        
        # 当长度小于4或两个字符串相同时，直接返回True
        if n < 4 or s1 == s2:
            return True
        
        f = self.isScramble
        # 尝试分割s1和s2进行递归判断
        for i in range(1, n):
            # 检查是否可以通过重新排列部分子字符串来构成另一个字符串
            if (f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or 
                f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i])):
                return True
        
        # 如果所有分割方式都不满足条件，则返回False
        return False

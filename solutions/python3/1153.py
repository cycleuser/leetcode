
class Solution:
    def canConvert(self, s1: str, s2: str) -> bool:
        """
        判断s1是否可以通过重新排列字母变成s2
        
        英文注释：Determine if s1 can be rearranged to form s2.
        """

        # 如果两个字符串相同，直接返回True
        if s1 == s2: 
            return True

        dp = {}
        
        # 使用字典记录s1中的字符及其对应在s2中的位置
        for i, j in zip(s1, s2):
            if dp.setdefault(i, j) != j:
                return False
        
        # 如果s2中所有字符都不同，则可以转换，因为最多只有26个小写字母
        return len(set(s2)) < 26

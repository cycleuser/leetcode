
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        
        中文注释：
        判断给定字符串是否可以通过重复某个子串构成。
        
        英文注释：
        Determine whether the given string can be constructed by repeating a substring.
        """

        # 检查字符串长度是否大于1，确保有足够字符进行分割
        if len(s) > 1:
            # 遍历可能的分隔因子i（从2到s长度-1）
            for i in range(2, len(s)):
                # 如果s的长度能被i整除，则进一步检查
                if len(s) % i == 0:
                    # 检查是否可以通过重复s[:i]构成整个字符串s
                    if s == (s[:i] * (len(s) // i)):
                        return True

        # 如果没有找到合适的子串，返回False
        return False

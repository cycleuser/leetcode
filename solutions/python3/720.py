
class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        
        英文注释：Given a list of strings, find the longest string that is composed only of 
                  valid prefixes present in the input list. If there are multiple such
                  strings of the same length, return any one of them.
        
        中文注释：给定一个字符串列表，找出由输入列表中的有效前缀组成的最长字符串。如果有多个相同长度的符合要求的字符串，
                  返回任意一个即可。
        """
        # 优化：使用集合存储words以提高查找速度
        word_set = set(words)
        
        for w in sorted(words, key=lambda x: (-len(x), x)):
            # 检查w的所有前缀是否都在word_set中（除了w本身）
            if all(w[:i] in word_set - {w} for i in range(1, len(w))):
                return w
        return ""

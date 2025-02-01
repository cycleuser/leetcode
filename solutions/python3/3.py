
class Solution:
    # 定义一个方法，用于计算最长不含重复字符的子串长度
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str  # 输入字符串s
        :rtype: int   # 返回最长不含重复字符的子串长度
        """

        max_len, start, char_map = 0, 0, {}  # 初始化最大长度，起始位置和字符索引映射字典

        for i in range(len(s)):
            # 如果当前字符已经在映射字典中，并且其上次出现的位置在当前起始位置之前或等于
            if s[i] in char_map and start <= char_map[s[i]]:
                # 更新起始位置为该字符上一次出现位置的下一个位置
                start = char_map[s[i]] + 1
            else:
                # 更新最大长度，确保每次都是当前子串的最新长度
                max_len = max(max_len, i - start + 1)

            # 更新字符映射字典
            char_map[s[i]] = i

        return max_len  # 返回最长不含重复字符的子串长度

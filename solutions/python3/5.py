
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 检查并扩展回文子串的辅助函数，英文：Helper function to check and expand palindrome substring
        def check(l, r):
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        
        # 构建所有可能的回文子串，英文：Construct all possible palindrome substrings
        pals = [check(i, i) for i in range(len(s))] + \
               [check(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
        
        # 返回最长的回文子串，英文：Return the longest palindrome substring
        return sorted(pals, key=len)[-1] if pals else ''

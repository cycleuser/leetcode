
class Solution:
    def largeGroupPositions(self, S: str) -> list[list[int]]:
        """
        寻找字符串中长度至少为3的相同字符连续子串的位置

        英文：
        Find the positions of substrings in a string where characters are consecutive and identical with length at least 3.
        """
        res = []  # 存储结果
        l = r = 0  # 初始化左右指针
        
        for i in range(1, len(S)):
            if S[i] == S[i - 1]:  # 如果当前字符和前一个相同，右指针r加一
                r += 1
            elif r - l >= 2 and (S[i] != S[i - 1] or i == len(S) - 1):  # 当满足条件时，记录子串位置
                res.append([l, r])
            if S[i] != S[i - 1]:  # 如果当前字符和前一个不同，重置左右指针
                l = r = i
        
        return res  # 返回结果

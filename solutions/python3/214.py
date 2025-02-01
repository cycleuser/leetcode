
class Solution:
    def shortestPalindrome(self, s, pre=""):
        """
        :param s: 输入字符串
        :param pre: 辅助变量，用于存储前缀反转结果，默认为空字符串
        :return: 返回最短回文串
        """
        for i in range(1, len(s) // 2 + 2):
            # 检查从当前索引开始的子串是否为之前部分的反转
            if s[i - 1:].startswith(s[:i][::-1]):
                pre = s[2 * i - 1:][::-1]
            # 同上，检查从当前索引之后的子串是否为之前部分的反转
            elif s[i:].startswith(s[:i][::-1]):
                pre = s[2 * i:][::-1]
        return pre + s


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        from collections import Counter  # 导入计数器模块

        # 统计字符出现次数，计算偶数次的字符总数
        out = even = sum(v for k, v in Counter(s).items() if v % 2 == 0)

        # 找出所有奇数次出现且大于1次的字符数量
        odd_big = [v for k, v in Counter(s).items() if v % 2 != 0 and v > 1]

        # 找出只出现一次的字符数量
        odd_small = [v for k, v in Counter(s).items() if v == 1]

        # 如果只有一个奇数次出现且大于1次的字符，则结果加该值
        if len(odd_big) == 1:
            out += odd_big[0]
        else:
            # 计算所有奇数次出现且大于1次的字符数量之和减去个数再加一
            out += sum(odd_big) - len(odd_big) + 1

            # 如果没有只出现一次的字符且没有奇数次出现且大于1次的字符，则结果减一
            if len(odd_small) == 0 and len(odd_big) == 0:
                out -= 1

        return out

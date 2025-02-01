
class Solution:
    # 定义一个名为findLUSlength的方法，用于查找两个字符串中不存在公共子序列的最大长度
    def findLUSlength(self, a: str, b: str) -> int:
        """
        :param a: 字符串a
        :type a: str
        :param b: 字符串b
        :type b: str
        :return: 如果两个字符串相等则返回-1，否则返回两者长度的最大值
        :rtype: int
        """
        # 如果两个字符串相同，则不存在公共子序列，直接返回-1
        if a == b:
            return -1
        else:
            # 否则返回两个字符串长度中的较大者
            return max(len(a), len(b))

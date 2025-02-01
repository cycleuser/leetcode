
class Solution:
    # 将Excel列标题转换为对应的数字，例如'A' -> 1, 'Z' -> 26, 'AA' -> 27, 等等。
    def titleToNumber(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # 反向遍历字符串，计算每个字符对应的权重值并累加结果
        return sum([(ord(char)-64)*(26**i) for i,char in enumerate(s[::-1])])

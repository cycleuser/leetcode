
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        """
        构造一个字符串，使得其中任意连续的字符数量不超过2个。
        
        中文注释：构造一个字符串，确保其中任何连续的字符数量都不超过两个。
        """
        if not A and not B: 
            return ''
        # 当A的数量大于等于B时
        if A >= B:
            a = 2 if A >= 2 else 1  # 确定a的值，最多用2个'a'
            b = 2 if A - a - B < 1 and B >= 2 else 1 if B else 0  # 确定b的值，如果剩余条件满足，则使用2个'b', 否则为1或0
            return a * 'a' + b * 'b' + self.strWithout3a3b(A - a, B - b)  # 递归构造剩余部分
        else:
            b = 2 if B >= 2 else 1  # 确定b的值，最多用2个'b'
            a = 2 if B - b - A < 1 and A >= 2 else 1 if A else 0  # 确定a的值，如果剩余条件满足，则使用2个'a', 否则为1或0
            return b * 'b' + a * 'a' + self.strWithout3a3b(A - a, B - b)  # 递归构造剩余部分

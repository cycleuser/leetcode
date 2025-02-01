
class Solution:
    # 计算n!的末尾零个数，使用递归方式
    def trailingZeroes(self, n: int) -> int:
        """
        :param n: 输入整数 n
        :return: 返回 n! 末尾零的个数
        
        例如：
        >>> Solution().trailingZeroes(5)
        1
        >>> Solution().trailingZeroes(20)
        4
        """
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)

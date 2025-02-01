
class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int

        输入一个整数n，返回将其变为1所需的最少操作次数。每次操作可以是将当前数字除以2（如果为偶数）或加减1使其变为偶数。
        - 若n等于1，则无需任何操作，直接返回0。
        - 如果n为偶数，则递归调用自身处理n/2，并将结果加1作为当前操作次数。
        - 如果n为奇数，则分别尝试n+1和n-1两种情况，取最小的操作次数并加1。
        """
        if n == 1: 
            return 0
        elif n % 2 == 0: 
            return self.integerReplacement(n // 2) + 1
        else: 
            return min(self.integerReplacement(n+1), self.integerReplacement(n-1)) + 1

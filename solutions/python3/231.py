
class Solution:
    def isPowerOfTwo(self, n):
        """
        判断一个整数是否为2的幂次方

        :param n: int - 需要判断的整数
        :return: bool - 如果n是2的幂次方，返回True；否则返回False
        """
        i = 0
        while 2 ** i <= n:
            if 2 ** i == n:
                return True
            i += 1
        return False

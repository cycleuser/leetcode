
class Solution:
    def findComplement(self, num):
        """
        :type num: int  # 输入整数num
        :rtype: int      # 返回补码
        """
        return int("".join([str((int(i)+1)%2) for i in bin(num)[2:]]), 2)  # 计算补码并转换为十进制返回

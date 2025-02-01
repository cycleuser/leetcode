
class Solution:
    def addDigits(self, num):
        """
        :type num: int  # 输入的数字
        :rtype: int      # 返回的结果，即所有位数之和连续求和直至结果为一位数
        """
        num = str(num)
        while len(num) > 1:
            num = str(sum([int(i) for i in num]))  # 将字符串转换为整数列表并求和后再次转换为字符串
        return int(num)  # 返回最终的结果

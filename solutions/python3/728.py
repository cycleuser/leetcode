
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        """
        :param left: 左边界（整数）
        :param right: 右边界（整数）
        :return: 在左闭右闭区间 [left, right] 内的所有自除数
        自除数是指可以被它包含的每一位数整除的数。
        
        :example:
            left = 1, right = 22
            返回值：[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
        """
        return [num for num in range(left, right + 1) if len([char for char in str(num) if int(char) != 0 and num % int(char) == 0]) == len(str(num))]

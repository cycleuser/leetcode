
class Solution:
    # 计算具有唯一数字的数的数量

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 使用预计算数组来提高效率，避免多次重复计算
        unique_digit_counts = [1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851, 5611771, 8877691]

        # 返回预计算数组中对应位置的值
        return unique_digit_counts[n % 11]

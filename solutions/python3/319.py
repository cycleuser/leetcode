
class Solution:
    # 返回从1到n中亮着的灯的数量
    # English: Return the number of bulbs that are on from 1 to n

    def bulbSwitch(self, n: int) -> int:
        # 计算小于等于n的最大整数平方根，即为最终亮着的灯的数量
        # English: Calculate the integer square root of n, which is the final number of bulbs that remain on.
        return int(n ** 0.5)

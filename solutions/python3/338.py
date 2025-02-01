
class Solution:
    # 计算0到num之间每个数的二进制表示中1的个数
    def countBits(self, num: int) -> List[int]:
        return [bin(i)[2:].count('1') for i in range(num + 1)]

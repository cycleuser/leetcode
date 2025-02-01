
class Solution:
    # 计算两个整数之间的汉明距离，即二进制表示下对应位不同的位数

    def hammingDistance(self, x: int, y: int) -> int:
        # 将两个整数转换为32位的二进制字符串，并确保长度相同
        bin_x = bin(x)[2:].zfill(32)
        bin_y = bin(y)[2:].zfill(32)

        # 计算对应位不同的位数，返回汉明距离
        return sum(a != b for a, b in zip(bin_x, bin_y))

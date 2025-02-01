
class Solution:
    # 判断给定整数的二进制表示中是否每一位都是交替出现的不同位

    def hasAlternatingBits(self, n: int) -> bool:
        # 将整数n转换为二进制字符串，并去掉前缀'0b'
        binary_str = bin(n)[2:]
        
        # 使用zip函数将二进制字符串的相邻字符配对
        # 检查每一对是否不同，即交替位条件是否满足
        return all(a != b for a, b in zip(binary_str, binary_str[1:]))

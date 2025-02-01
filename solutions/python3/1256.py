
class Solution:
    # 中文注释：实现整数到二进制字符串的编码，去掉前导'0b'和第一个字符'1'
    # English comment: Implement integer to binary string encoding, removing the leading '0b' and the first character '1'
    
    def encode(self, num: int) -> str:
        return bin(num + 1)[3:]

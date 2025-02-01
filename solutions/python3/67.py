
class Solution:
    # 将二进制字符串a和b相加并返回结果的二进制表示形式
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]  # 直接转换为十进制后相加，再转回二进制去除前缀'0b'



class Solution:
    # 将二进制字符串a和b相加并返回结果的二进制表示形式
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]  # 直接转换为十进制后相加，再转回二进制去除前缀'0b'

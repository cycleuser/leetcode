
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        """
        :type a: str  # 输入字符串a，例如 "2+3i"
        :type b: str  # 输入字符串b，例如 "4+5i"
        :rtype: str   # 返回结果字符串，例如 "13+14i"
        
        实现两个复数的乘法运算。
        """
        real_a, imag_a = map(int, a[:-1].split("+"))
        real_b, imag_b = map(int, b[:-1].split("+"))
        
        real_part = real_a * real_b - imag_a * imag_b
        imag_part = real_a * imag_b + real_b * imag_a
        
        return f"{real_part}+{imag_part}i"

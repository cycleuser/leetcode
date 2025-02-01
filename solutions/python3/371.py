    
class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # mx 为正数的最大值，mask 用于防止溢出
        # Python 中没有整型溢出的概念，但为了模拟类似行为使用 mask
        mx, mask = 0x7FFFFFFF, 0xFFFFFFFF
        
        # 使用异或和与运算来模拟加法
        while b:
            # a 记录当前的未进位部分，b 记录当前的进位部分
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        # 返回结果，注意 Python 中没有溢出，这里只是模拟
        return a if a <= mx else ~(a ^ mask)
    
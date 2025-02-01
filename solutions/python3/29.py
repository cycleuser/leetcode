
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        :type dividend: int 被除数
        :type divisor: int 除数
        :rtype: int 返回结果
        """
        
        # 判断正负号
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        
        while dividend >= divisor:
            temp, i = divisor, 1
            # 快速减法，二进制左移实现快速计算
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
                
        if not positive: 
            res = -res
        
        return min(max(-2 ** 31, res), 2 ** 31 - 1)



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        :type dividend: int 被除数
        :type divisor: int 除数
        :rtype: int 返回结果
        """
        
        # 判断正负号
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        
        while dividend >= divisor:
            temp, i = divisor, 1
            # 快速减法，二进制左移实现快速计算
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
                
        if not positive: 
            res = -res
        
        return min(max(-2 ** 31, res), 2 ** 31 - 1)

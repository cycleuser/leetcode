
class Solution:
    # 定义一个类，用于解决位运算问题
    
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 该方法接受两个整数m和n作为输入，返回它们之间的按位与结果
        
        i = 0
        # 初始化计数器i为0，用于记录右移次数
        
        while m != n:
            # 当m和n不相等时循环
            
            m >>= 1
            # 将m右移一位
            
            n >>= 1
            # 将n右移一位
            
            i += 1
            # 计数器i加1，记录右移次数
        
        return m << i
        # 返回m左移i位的结果，即为m和n之间的按位与结果

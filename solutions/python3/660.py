
class Solution:
    # 新建一个类，用于处理进制转换
    
    def newInteger(self, n: int) -> int:
        # 将十进制整数n转换为九进制字符串表示
        
        base9 = ""
        while n:
            # 计算当前数字除以9的余数，并将其转换为字符形式添加到base9中
            base9 += str(n % 9)
            # 整除操作，减少当前处理的数值
            n //= 9
            
        # 返回九进制字符串反转后的整数值
        return int(base9[::-1])


class Solution:
    # 定义一个类来处理负二进制转换

    def baseNeg2(self, n: int) -> str:
        # 初始化位列表，用于存储每一位的结果
        bits = []
        
        while n != 0:
            # 使用divmod进行除法运算，并得到商和余数
            n, rem = divmod(n, -2)
            
            # 如果余数小于0，则调整n和rem的值
            if rem < 0:
                n += 1
                rem -= -2
            
            # 将当前位转换为字符串形式并添加到bits列表中
            bits.append(str(rem))
        
        # 如果没有生成任何位，返回'0'
        return "".join(bits[::-1]) if bits else '0'



class Solution:
    # 定义一个类来处理负二进制转换

    def baseNeg2(self, n: int) -> str:
        # 初始化位列表，用于存储每一位的结果
        bits = []
        
        while n != 0:
            # 使用divmod进行除法运算，并得到商和余数
            n, rem = divmod(n, -2)
            
            # 如果余数小于0，则调整n和rem的值
            if rem < 0:
                n += 1
                rem -= -2
            
            # 将当前位转换为字符串形式并添加到bits列表中
            bits.append(str(rem))
        
        # 如果没有生成任何位，返回'0'
        return "".join(bits[::-1]) if bits else '0'

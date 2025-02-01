
class Solution:
    def calculate(self, s: str) -> int:
        # 计算两个数根据运算符的加减操作
        def calc(n2: int, op: str, n1: int) -> int:
            return n1 + n2 if op == "+" else n1 - n2

        stack = []  # 用于存储中间结果和操作符
        i, num = 0, 0  # 遍历字符串的索引与当前数字
        
        while i < len(s):
            j = i
            # 将连续的数字转换为整数并记录位置
            while j < len(s) and s[j].isdigit():
                num, j = num * 10 + int(s[j]), j + 1
            
            if i != j:
                # 如果当前字符不是数字，说明之前解析了一个数字，进行计算
                stack.append(calc(num, stack.pop(), stack.pop()) 
                             if stack and s[i - 1] != "(" else num)
                num, j = 0, j - 1
            elif s[i] in "+-":
                # 遇到加减号，直接压入栈中
                stack.append(s[i])
            elif s[i] == ")" and len(stack) > 1:
                # 当遇到右括号时，进行相应的计算操作
                stack.append(calc(stack.pop(), stack.pop(), stack.pop()))
            
            i = j + 1
        
        return stack.pop()  # 最终结果在栈顶

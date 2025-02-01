
class Solution:
    def calculate(self, s: str) -> int:
        # 计算表达式s的结果，支持基本的加减乘除运算
        def calculate_expression(expression: list) -> int:
            # 递归计算栈中的表达式结果
            stack = []
            i = 0
            n = len(expression)
            
            while i < n:
                if expression[i] == " ": 
                    i += 1
                    continue
                
                while i < n and expression[i].isnumeric():
                    num += expression[i]
                    i += 1

                if stack and (stack[-1] in ["*", "/", "+", "-"]):
                    op = stack.pop()
                    num1 = stack.pop()

                    if op == "*":
                        stack.append(num1 * int(num))
                    elif op == "/":
                        stack.append(int(num1 / int(num)))
                    elif op == "+":
                        stack.append(num1 + int(expression[i]))
                        i += 1
                    else:
                        stack.append(num1 - int(expression[i]))
                        i += 1

                    num = ""
                
                elif num: 
                    stack.append(int(num))
                    num = ""

                else:
                    stack.append(expression[i])
                    i += 1
            
            return sum(stack)
        
        # 初始处理
        mod = 0
        
        while mod < 2:
            stack, i, n, num = [], 0, len(s), ""
            
            s = calculate_expression(list(s))
            
            mod += 1

        return s.pop()



class Solution:
    def calculate(self, s: str) -> int:
        # 计算表达式s的结果，支持基本的加减乘除运算
        def calculate_expression(expression: list) -> int:
            # 递归计算栈中的表达式结果
            stack = []
            i = 0
            n = len(expression)
            
            while i < n:
                if expression[i] == " ": 
                    i += 1
                    continue
                
                while i < n and expression[i].isnumeric():
                    num += expression[i]
                    i += 1

                if stack and (stack[-1] in ["*", "/", "+", "-"]):
                    op = stack.pop()
                    num1 = stack.pop()

                    if op == "*":
                        stack.append(num1 * int(num))
                    elif op == "/":
                        stack.append(int(num1 / int(num)))
                    elif op == "+":
                        stack.append(num1 + int(expression[i]))
                        i += 1
                    else:
                        stack.append(num1 - int(expression[i]))
                        i += 1

                    num = ""
                
                elif num: 
                    stack.append(int(num))
                    num = ""

                else:
                    stack.append(expression[i])
                    i += 1
            
            return sum(stack)
        
        # 初始处理
        mod = 0
        
        while mod < 2:
            stack, i, n, num = [], 0, len(s), ""
            
            s = calculate_expression(list(s))
            
            mod += 1

        return s.pop()


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # 使用栈来处理逆波兰表达式
        stack = []
        
        for token in tokens:
            # 如果当前token不是操作符，则将其转化为整数并压入栈中
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                # 弹出两个数字进行运算
                num2, num1 = stack.pop(), stack.pop()
                
                # 根据操作符执行相应的数学运算，并将结果重新压入栈中
                if token == "+":
                    last = num1 + num2
                elif token == "-":
                    last = num1 - num2
                elif token == "*":
                    last = num1 * num2
                elif token == "/":
                    # 由于除法可能产生浮点数，所以使用int()函数将结果转换为整型
                    last = int(num1 / num2)
                
                stack.append(last)
        
        # 最后栈中仅剩一个元素即为计算结果
        return stack[0]


class Solution:
    # 计算器函数，用于进行基本运算
    def calculate(self, s: str) -> int:
        # 辅助函数：执行两个数字的计算
        def calc(n2, op, n1): 
            return n1 * n2 if op == '*' else n1 // n2 if op == '/' else n1 + n2 if op == '+' else n1 - n2
        
        # 辅助函数：处理数组中的运算，进行计算
        def calc2(arr):
            if len(arr) == 1:
                return arr.pop()
            res = arr[0]
            for j in range(2, len(arr), 2):
                res = calc(arr[j], arr[j - 1], res)
            return res
        
        # 初始化栈和索引
        stack, i, num = [], 0, 0
        
        while i < len(s):
            j = i
            # 解析数字部分
            while j < len(s) and s[j].isdigit():
                num, j = num * 10 + int(s[j]), j + 1
            
            if i != j:
                # 如果有运算符，进行计算并入栈
                stack.append(calc(num, stack.pop(), stack.pop()) if stack and stack[-1] in "*/" else num)
                num, j = 0, j - 1
            elif s[i] == ")":
                # 处理括号
                ind = len(stack) - stack[::-1].index('(') - 1
                stack[ind:] = [calc2(stack[ind + 1:])]
                if len(stack) > 1 and stack[-2] in '*/':
                    stack.append(calc(stack.pop(), stack.pop(), stack.pop()))
            elif s[i] != ' ':
                # 将非空格字符入栈
                stack.append(s[i])
            i = j + 1
        
        return calc2(stack)

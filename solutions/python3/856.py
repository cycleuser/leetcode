
class Solution:
    # 定义一个求括号分数的方法
    def scoreOfParentheses(self, S: str) -> int:
        # 初始化栈和结果变量
        stack, res = [], 0
        
        for c in S:
            if c == "(":
                # 当遇到左括号时，将其对应的右括号的分值设为0并入栈
                stack.append(0)
            else:
                # 遇到右括号时计算当前子表达式的分数
                add = 2 * stack.pop() or 1
                
                if stack:
                    # 如果栈不为空，将计算的结果加在栈顶元素上
                    stack[-1] += add
                else:
                    # 如果栈为空，则将结果累加到res中
                    res += add
        
        return res

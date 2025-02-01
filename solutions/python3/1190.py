
class Solution:
    # 定义一个类来解决问题
    
    def reverseParentheses(self, s: str) -> str:
        # 实现翻转括号内的子字符串的方法
        
        stack = ['']  # 初始化栈，用于存储当前层的字符串片段
        
        for c in s:
            if c == '(':
                # 遇到左括号时，将新的空字符串加入栈中
                stack.append('')
            elif c == ')':
                # 遇到右括号时，取出栈顶元素并翻转其内容添加回上一层的字符串片段中
                add = stack.pop()[::-1]
                stack[-1] += add
            else:
                # 如果是普通字符，则直接追加到当前层的字符串片段中
                stack[-1] += c
        
        return stack.pop()  # 最终返回结果字符串

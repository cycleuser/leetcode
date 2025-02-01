
class Solution:
    # 解决器类

    def removeDuplicates(self, S: str) -> str:
        # 移除字符串中的重复字符
        stack = []  # 初始化栈
        
        for s in S:  # 遍历输入字符串S的每一个字符s
            if stack and stack[-1] == s:  # 如果栈顶元素和当前字符相同
                stack.pop()  # 弹出栈顶元素
            else:
                stack.append(s)  # 否则将当前字符压入栈中
        
        return ''.join(stack)  # 将栈中的字符拼接成字符串并返回

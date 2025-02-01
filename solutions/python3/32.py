
class Solution:
    def longestValidParentheses(self, s):
        """
        :param s: 输入字符串，包含括号 '()'。
        :return: 返回最长有效括号序列的长度。
        
        使用栈来存储索引，遍历字符串时遇到左括号入栈，右括号匹配成功出栈；否则将当前索引入栈。最后通过计算相邻索引差值获取最大有效括号长度。
        """
        stack, mx = [], 0
        for i, c in enumerate(s):
            if c == ")" and stack and s[stack[-1]] == "(":  # 右括号匹配成功，出栈
                stack.pop()
            else:  # 入栈当前索引或左括号
                stack.append(i)
        
        # 在栈中添加哨兵节点 -1 和字符串长度 len(s)，方便后续计算间隔
        stack = [-1] + stack + [len(s)]
        
        # 计算相邻索引差值，更新最大有效括号序列的长度 mx
        for i1, i2 in zip(stack, stack[1:]):
            mx = max(mx, i2 - i1 - 1)
        
        return mx if len(stack) > 2 else len(s)

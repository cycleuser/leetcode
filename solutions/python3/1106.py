
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        """
        解析布尔表达式并返回结果。
        
        :param expression: 字符串形式的布尔表达式，包含 't', 'f', '&' 和 '|'
        :return: 解析后的布尔值
        """
        stack = []
        for c in expression:
            if c == ')':
                """
                遇到右括号时，进行以下操作：
                1. 将缓存列表中的元素弹出并计算结果。
                2. 根据栈顶运算符决定使用 all 还是 any 方法处理缓存列表的结果。
                3. 将最终计算结果压入栈中，并弹出当前括号。
                """
                cache = []
                while stack[-1] != '(':
                    cache.append(stack.pop())
                stack.pop()
                cur = stack.pop()
                if cur == '&':
                    stack.append(all(cache))
                elif cur == '|':
                    stack.append(any(cache))
                else:  # cur == '!'
                    stack.append(not cache.pop())
            elif c != ',':
                """
                遇到非逗号字符时，将其转换为布尔值并压入栈中：
                - 't' 对应 True
                - 'f' 对应 False
                - 其他直接作为运算符压入
                """
                stack.append(True if c == 't' else False if c == 'f' else c)
        return stack.pop()

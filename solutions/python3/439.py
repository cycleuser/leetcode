
class Solution:
    def parseTernary(self, expression: str, stack: list = []) -> bool:
        """
        解析三元表达式

        :param expression: 三元表达式的字符串形式，例如 "T?1:0"
        :param stack: 用于存储中间结果的栈
        :return: 解析后的布尔值结果
        """
        for c in expression[::-1]:
            # 中文注释：检查当前元素是否为问号，并且栈顶是否为"?"，如果是则解析三元表达式
            if stack and stack[-1] == "?":
                _, first, q, second = stack.pop(), stack.pop(), stack.pop(), stack.pop()
                stack.append(c == "T" and first or second)
            else:
                # 中文注释：将当前元素压入栈中
                stack.append(c)
        return stack.pop()  # 返回最终结果，中文注释：从栈顶弹出并返回解析后的布尔值结果

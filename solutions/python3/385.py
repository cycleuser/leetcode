
class Solution:
    def deserialize(self, s: str) -> 'NestedInteger':
        """
        Deserialize a nested list from a string representation.
        
        中文注释：将字符串表示的嵌套列表反序列化。
        """

        stack, num, last = [], "", None

        for c in s:
            if c.isdigit() or c == "-":
                # 数字或负号，累加形成数字
                num += c
            elif c == "," and num:
                # 逗号且之前有数字，将数字添加到栈顶元素的子列表中
                stack[-1].add(NestedInteger(int(num)))
                num = ""
            elif c == "[":
                # 左括号，创建新元素并压入栈
                elem = NestedInteger()
                if stack: 
                    stack[-1].add(elem)
                stack.append(elem)
            elif c == "]":
                # 右括号且之前有数字，将数字添加到当前元素中
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
                # 弹出栈顶元素作为结果的最终部分
                last = stack.pop()

        return last if last else NestedInteger(int(num))

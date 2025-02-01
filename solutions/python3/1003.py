
class Solution:
    # 判断字符串S是否由合法的"abc"子串组成
    def isValid(self, S: str) -> bool:
        stack = []
        for i in S:
            # 如果当前字符是 'c'
            if i == 'c':
                # 检查栈顶两个元素是否为 'a' 和 'b'
                if stack[-2:] != ['a', 'b']:
                    return False
                # 弹出栈顶的 'b'
                stack.pop()
                # 再弹出栈顶的 'a'
                stack.pop()
            else:
                # 其他字符直接入栈
                stack.append(i)
        # 栈为空则表示所有合法子串匹配成功
        return not stack

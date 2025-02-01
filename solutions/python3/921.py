
class Solution:
    # 定义一个类来解决最小添加使括号有效的问题

    def minAddToMakeValid(self, S):
        # r 记录需要添加的右括号数量，l 列表用来辅助匹配左括号和右括号
        r, l = 0, []
        
        for s in S:
            if s == "(":
                # 遇到左括号时将其入栈（列表）
                l.append(s)
            elif l:  # 如果此时栈不为空，说明可以匹配一个右括号
                l.pop()
            else:
                # 栈为空且遇到右括号时，需要增加的右括号数量加一
                r += 1 

        # 最终返回需要添加的左右括号总数
        return r + len(l)

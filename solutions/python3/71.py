
class Solution:
    # 定义一个简化路径的方法
    def simplifyPath(self, path):
        # 使用栈来存储路径中的有效部分
        stack = []
        
        # 遍历分割后的路径字符串列表
        for c in path.split("/"):
            # 如果遇到'..'且栈非空，弹出栈顶元素
            if c == "..":
                if stack:
                    stack.pop()
            # 如果当前字符有效（不为空且不是'.')，则压入栈中
            elif c and c != ".":
                stack.append(c)
        
        # 最终的简化路径为栈内所有元素拼接而成，并以'/'开头
        return "/" + "/".join(stack)

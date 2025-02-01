
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 将字符串表示的二叉树转换为实际的树节点结构
    def str2tree(self, s: str) -> TreeNode:
        stack, cur = [], ""
        
        for i, c in enumerate(s):
            if c.isnumeric() or c == "-":
                # 如果当前字符是数字或负号，累积构建当前节点值
                cur += c
            elif not cur:
                # 当前节点值未初始化时
                if c == ")":
                    # 遇到右括号时，弹出栈顶节点（结束当前子树）
                    stack.pop()
            else:
                # 当前节点值已累积完成
                node = TreeNode(int(cur))
                # 将构建好的节点添加到父节点下
                if stack:
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                
                cur = ""  # 重置累积字符串
                if c == "(":
                    # 遇到左括号时，将节点压入栈中（开始构建子树）
                    stack.append(node)
        
        # 返回根节点或空树
        return stack and stack[0] or (cur and TreeNode(int(cur))) or []

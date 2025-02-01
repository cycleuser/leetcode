
class Solution:
    # 定义一个从先序遍历序列构建二叉搜索树的方法
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # 根节点初始化为先序遍历的第一个元素
        root = TreeNode(preorder[0])
        # 使用栈来维护当前的父节点列表，初始时包含根节点
        stack = [root]
        
        for value in preorder[1:]:
            # 如果当前值小于栈顶节点，则将其作为左子节点
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                # 否则，弹出栈中所有小于当前值的节点，并将当前值作为最后一个弹出节点的右子节点
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        
        return root

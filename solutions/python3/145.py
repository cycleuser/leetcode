
class Solution:
    def postorderTraversal(self, root):
        """
        中文注释：此函数用于实现二叉树的后序遍历。
        英文注释: This function is used to implement the post-order traversal of a binary tree.
        
        :param root: 二叉树的根节点
        :return: 返回后序遍历的结果列表
        """
        ret, stack = [], root and [root]
        while stack:
            node = stack.pop()
            ret.append(node.val)
            # 将右子节点和左子节点依次压入栈中，确保先处理左子树
            stack += [child for child in (node.right, node.left) if child]
        return ret[::-1]  # 反转列表以获得正确的后序遍历结果

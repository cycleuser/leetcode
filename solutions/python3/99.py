
class Solution:
    def recoverTree(self, root):
        """
        修复二叉搜索树中两个错误节点的值以恢复正确的排序。
        
        :param root: 二叉搜索树的根节点
        """

        def inorder(node):
            """
            中序遍历生成器，用于迭代访问二叉搜索树中的每个节点。

            :param node: 当前访问的节点
            """
            if node.left:
                yield from inorder(node.left)
            yield node
            if node.right:
                yield from inorder(node.right)

        swap1 = swap2 = smaller = None
        for node in inorder(root):
            """
            遍历二叉搜索树中的每个节点，找到需要交换的两个节点。

            :param node: 当前访问的节点
            """
            if smaller and smaller.val > node.val:
                if not swap1:
                    swap1 = smaller
                swap2 = node
            smaller = node

        if swap1:
            swap1.val, swap2.val = swap2.val, swap1.val

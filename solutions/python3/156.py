
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归反转二叉树，将左子节点变为新的根，并调整左右子树关系
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if root:
            # 递归处理左子树
            left = self.upsideDownBinaryTree(root.left)
            # 递归处理右子树，这里可以不返回结果直接修改root节点
            _ = self.upsideDownBinaryTree(root.right)

            # 当前根的左子节点变为新的根，并调整左右子树关系
            if root.left:
                new_root = root.left
                root.left.right, root.left.left = root, root.right
                root.right = root.left = None
                return new_root  # 返回新根节点
        # 如果root为空，直接返回None
        return root

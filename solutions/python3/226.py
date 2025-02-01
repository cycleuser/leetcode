
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归翻转二叉树的左右子节点
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: 
            return  # 如果根节点为空，直接返回

        # 交换当前节点的左、右子节点
        root.left, root.right = root.right, root.left

        # 递归翻转左右子树
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root  # 返回根节点，已完成翻转操作

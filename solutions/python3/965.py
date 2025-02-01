
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 检查是否为单值二叉树
    def isUnivalTree(self, root: 'TreeNode') -> 'bool':
        """
        :type root: TreeNode
        :rtype: bool
        
        English: Check if the binary tree is a univalue tree.
        
        Parameters:
            root (TreeNode): The root node of the binary tree
        
        Returns:
            bool: True if all nodes have the same value, False otherwise
        """
        # 如果根节点为空，返回True
        if not root:
            return True
        # 检查左子树是否为单值树且左子节点的值等于根节点值
        if root.left and root.left.val != root.val:
            return False
        # 检查右子树是否为单值树且右子节点的值等于根节点值
        if root.right and root.right.val != root.val:
            return False
        # 递归检查左、右子树是否为单值树
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 修剪二叉搜索树，使所有节点的值位于[L, R]之间
    # @param {TreeNode} root 树根节点
    # @param {int} L 下限值
    # @param {int} R 上限值
    # @return {TreeNode} 返回修剪后的树根节点
    def trimBST(self, root: 'TreeNode', L: int, R: int) -> 'TreeNode':
        if not root:
            return
        
        # 递归处理左子树和右子树
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        
        # 如果当前节点值不在[L, R]范围内，则返回其符合条件的子节点
        if root.val > R or root.val < L:
            return root.left if root.left else root.right
        
        return root

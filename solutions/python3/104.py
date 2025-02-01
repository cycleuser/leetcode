
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 计算二叉树的最大深度
    def maxDepth(self, root: TreeNode, depth=0) -> int:
        # 如果节点不为空，则递归计算左右子树的深度，并取较大值加一；否则返回当前深度
        return max(self.maxDepth(root.left, depth + 1), self.maxDepth(root.right, depth + 1)) if root else depth

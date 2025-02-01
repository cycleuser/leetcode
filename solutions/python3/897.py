
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归构建一个单调递增的二叉树，尾节点初始为None
    def increasingBST(self, root: TreeNode, tail = None) -> TreeNode:
        if not root: 
            return tail  # 如果当前节点为空，则返回尾节点
        
        res = self.increasingBST(root.left, root)  # 先处理左子树
        
        root.left = None  # 清除左指针，确保单调性
        
        root.right = self.increasingBST(root.right, tail)  # 处理右子树，并将当前节点连接到新的尾部
        
        return res  # 返回重构后的根节点

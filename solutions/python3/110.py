
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 判断二叉树是否平衡，返回True或False
    # Judge whether the binary tree is balanced and return True or False
    def isBalanced(self, root: 'TreeNode') -> bool:
        # 如果高度计算结果不为-1，则说明树是平衡的
        # If height calculation result is not -1, then the tree is balanced
        return self.computeHeight(root) != -1
    
    # 计算节点高度，返回-1表示不平衡，否则返回高度
    # Calculate node height, return -1 if unbalanced, otherwise return height
    def computeHeight(self, node: 'TreeNode') -> int:
        if not node: 
            # 空节点高度为0
            # Height of an empty node is 0
            return 0
        
        left_h = self.computeHeight(node.left)
        right_h = self.computeHeight(node.right)
        
        # 如果左右子树高度差大于1或任一子树不平衡，则返回-1表示不平衡
        # If the height difference between left and right subtrees is greater than 1 or any subtree is unbalanced, return -1 indicating imbalance
        if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1: 
            return -1
        
        # 返回当前节点的高度，即左右子树较高者加一
        # Return the height of current node, which is the max height of its subtrees plus one
        return max(left_h, right_h) + 1

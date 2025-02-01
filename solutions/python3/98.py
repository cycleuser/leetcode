
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 检查二叉树是否为有效二叉搜索树
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def validate(node, mn, mx):
            """
            验证节点值是否在给定的范围内，并递归验证其左右子树。
            - node: 当前检查的节点
            - mn: 节点值必须大于该最小值
            - mx: 节点值必须小于该最大值
            :type node: TreeNode
            :type mn: int
            :type mx: int
            :rtype: bool
            """
            if not node: 
                return True
            if node.val < mn or node.val > mx: 
                return False
            return validate(node.left, mn, node.val-1) and validate(node.right, node.val+1, mx)
        
        return validate(root, -float("inf"), float("inf"))

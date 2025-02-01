
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    计算二叉树的最小深度
    """
    def minDepth(self, root: 'TreeNode') -> 'int':
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.compute(root)
    
    def compute(self, node):
        """
        递归计算节点的最小深度

        :param node: 当前处理的树节点
        :return: 节点子树的最小深度
        """
        if not node: 
            # 如果当前节点为空，返回0
            return 0
        
        left_d = self.compute(node.left)
        right_d = self.compute(node.right)

        if node.left and node.right:
            # 当左右孩子都不为空时，取较浅的那一个子树深度加1
            return min(left_d, right_d) + 1
        else: 
            # 当只有一个子节点或没有子节点时，返回非空子树深度加1
            return max(left_d, right_d) + 1

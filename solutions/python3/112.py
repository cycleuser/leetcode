
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 检查从根节点到叶子节点的路径和是否等于给定值sum
    def hasPathSum(self, root: 'TreeNode', sum: int) -> bool:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        
        Check if there is a path from the root to any leaf node where the sum of values equals the given sum.
        """
        # 如果根节点为空，返回False
        if not root: 
            return False

        # 减去当前节点的值
        sum -= root.val

        # 如果到达叶子节点且路径和等于0，则找到符合条件的路径
        if not root.left and not root.right and sum == 0:
            return True
        
        # 递归检查左子树或右子树
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

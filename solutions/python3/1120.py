
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    该类用于解决二叉树子树平均值最大问题。
    """

    def maximumAverageSubtree(self, node: TreeNode, parent=None) -> float:
        """
        计算以给定节点为中心的最大子树平均值。

        参数:
            node (TreeNode): 当前处理的节点
            parent (TreeNode): 父节点，用于避免重复计算

        返回:
            float: 最大子树平均值
        """

        # 如果当前节点为空，则返回0, 0, 0
        if not node:
            return 0, 0, 0
        
        # 递归处理左子树
        lCnt, lSum, lAvg = self.maximumAverageSubtree(node.left, node)
        
        # 递归处理右子树
        rCnt, rSum, rAvg = self.maximumAverageSubtree(node.right, node)

        # 计算当前节点为中心的最大平均值
        ret = max((node.val + lSum + rSum) / (lCnt + rCnt + 1), lAvg, rAvg)
        
        # 如果父节点为空，返回最大子树平均值；否则返回节点计数、总和和最大平均值元组
        return (lCnt + rCnt + 1, lSum + rSum + node.val, ret) if parent is None else ret

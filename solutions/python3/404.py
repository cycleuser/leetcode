
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 计算二叉树中所有左叶子节点的和
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """

        # 递归函数，用于遍历节点并收集左叶子节点值
        def left(node, sm):
            if not node:
                return

            # 递归处理左子树
            left(node.left, sm)

            # 检查当前节点的左子节点是否为叶节点
            if node.left and not node.left.left and not node.left.right:
                sm.append(node.left.val)

            # 递归处理右子树
            left(node.right, sm)
        
        # 初始化结果列表
        otp = list()
        # 调用递归函数开始遍历
        left(root, otp)
        # 返回所有左叶子节点值的和
        return sum(otp)

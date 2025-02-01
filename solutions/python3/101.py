
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x  # 节点的值
        self.left = None  # 左子节点
        self.right = None  # 右子节点

class Solution:
    """
    检查二叉树是否对称。
    
    :type root: TreeNode, 树的根节点
    :rtype: bool, 是否对称
    """

    def isSymmetric(self, root):
        """
        检查两棵子树是否互为镜像。

        :type left: TreeNode, 左子节点
        :type right: TreeNode, 右子节点
        :rtype: bool, 两子树是否互为镜像
        """
        if root is None:
            return True  # 空树是对称的

        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        """
        检查两棵子树是否互为镜像。
        
        :type left: TreeNode, 左子节点
        :type right: TreeNode, 右子节点
        :rtype: bool, 两子树是否互为镜像

        - 如果左右节点都为空，则互为镜像。
        - 如果仅有一个节点为空，或者节点值不同，则不互为镜像。
        - 否则检查左子树的左孩子和右子树的右孩子，以及左子树的右孩子和右子树的左孩子是否互为镜像。
        """
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPiar = self.isMirror(left.right, right.left)
            return outPair and inPiar
        else:
            return False

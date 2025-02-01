
class Solution:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        """
        合并两棵二叉树，将它们的节点值相加。
        
        :param t1: 第一棵二叉树的根节点
        :type t1: TreeNode
        :param t2: 第二棵树的根节点
        :type t2: TreeNode
        :return: 合并后的二叉树的根节点
        :rtype: TreeNode
        """
        if t1 and t2:
            # 创建新的根节点，值为两棵树根节点值之和
            root = TreeNode(t1.val + t2.val)
            # 递归合并左子树
            root.left = self.mergeTrees(t1.left, t2.left)
            # 递归合并右子树
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2

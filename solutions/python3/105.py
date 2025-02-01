
class Solution(object):
    """
    Definition for a binary tree node.
    """
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    """
    构建二叉树的方法。
    
    根据前序遍历和中序遍历来构建二叉树。
    """

    def buildTree(self, preorder, inorder):
        # 如果中序遍历列表不为空
        if inorder:
            # 找到当前根节点在中序遍历中的索引位置
            ind = inorder.index(preorder.pop(0))
            # 创建根节点
            root = self.TreeNode(inorder[ind])
            # 递归构建左子树
            root.left = self.buildTree(preorder, inorder[0:ind])
            # 递归构建右子树
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

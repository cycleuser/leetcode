
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 将二叉搜索树转换为累加树
    # Convert a binary search tree to a greater sum tree (累加树)
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def traverse(node):
            # 递归遍历右子树
            if not node: 
                return
            traverse(node.right)
            
            # 更新当前节点值为累加和
            node.val = residue[0] = node.val + residue[0]
            
            # 递归遍历左子树
            traverse(node.left)
        
        # 初始化累加和列表
        residue = [0]
        
        # 调用遍历函数并返回结果
        return traverse(root)


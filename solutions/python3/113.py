
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 查找二叉树中所有满足路径和等于给定值的路径
    def pathSum(self, root: 'TreeNode', sum: int) -> 'List[List[int]]':
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        # 递归函数，用于遍历树并查找所有路径和等于给定值的路径
        def traverse(node, q, residue):
            if node:
                # 如果当前节点是叶子节点且路径和等于目标值，则将当前路径加入结果中
                if not node.left and not node.right and residue + node.val == sum: 
                    return [q + [node.val]]
                else:
                    # 递归遍历左子树和右子树，累加当前节点的值到路径中
                    left_paths = traverse(node.left, q + [node.val], residue + node.val)
                    right_paths = traverse(node.right, q + [node.val], residue + node.val)
                    return left_paths + right_paths
            else:
                # 如果当前节点为空，返回空列表
                return []
        
        # 从根节点开始遍历树并查找所有路径和等于给定值的路径
        return traverse(root, [], 0)

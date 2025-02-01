
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    该类用于计算二叉树中从根节点到叶子节点的数字之和。
    英文：This class is used to calculate the sum of numbers from root to leaf nodes in a binary tree.
    """

    def sumNumbers(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        计算从根节点到叶子节点的数字之和。
        英文：Calculate the sum of numbers from the root node to leaf nodes.
        """
        
        # 递归函数，用于遍历树并构建路径字符串
        def traverse(node, q):
            """
            递归遍历节点，并将当前节点值加入路径列表中。
            如果到达叶子节点，则将该路径对应的数字加到结果中。
            英文：Recursive function to traverse nodes and add current node value to the path list.
                   If it reaches a leaf node, add the number corresponding to this path to the result.
            """
            if not node: 
                return
            q.append(str(node.val))  # 将当前节点值加入路径列表中
            if not node.left and not node.right: 
                res[0] += int("".join(q))  # 如果是叶子节点，则将路径字符串转换为数字并加到结果中
            traverse(node.left, q)  # 递归遍历左子树
            traverse(node.right, q)  # 递归遍历右子树
        
        res = [0]  # 存储最终的结果
        traverse(root, [])  # 从根节点开始遍历
        return res[0]

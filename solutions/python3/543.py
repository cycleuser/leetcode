
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 计算二叉树的最大直径
    def diameterOfBinaryTree(self, root: 'TreeNode') -> int:
        """
        :type root: TreeNode
        :rtype: int
        
        输入：
            - root: 二叉树的根节点
        输出：
            - 返回二叉树的最大直径
        
        思路：
            使用深度优先搜索（DFS）遍历每个节点，计算以该节点为根的左右子树的最大路径长度之和。
            更新全局最大值 res[0] 来记录整个树中的最大直径。
        """
        res = [0]

        def traverse(node):
            # 如果当前节点为空，返回 0
            if not node: return 0

            # 递归遍历左右子树，并计算路径长度
            left, right = traverse(node.left), traverse(node.right)

            # 更新最大直径
            res[0] = max(left + right, res[0])

            # 返回当前节点的最大路径长度
            return 1 + max(left, right)
        
        traverse(root)
        return res[0]

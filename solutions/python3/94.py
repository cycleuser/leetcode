
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 中文: 实现二叉树的中序遍历
    # 英文: Implement in-order traversal of a binary tree
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        
        # 中文: 深度优先搜索函数，用于递归遍历节点
        # 英文: Depth-first search function for recursive node traversal
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return self.res

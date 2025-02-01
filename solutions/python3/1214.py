
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from functools import lru_cache

class Solution:
    # 二叉搜索树 root1 和 root2 中是否存在两个结点，使得它们的和为 target
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:

        # 深度优先遍历生成节点值集合
        @lru_cache(None)
        def dfs(node):
            return dfs(node.left) | dfs(node.right) | {node.val} if node else set()

        # 遍历 root1 生成的值集合
        q1 = dfs(root1)

        # 检查是否存在 target - a 在 q1 中，且 a 是遍历 root2 生成的值
        return any(target - a in q1 for a in dfs(root2))

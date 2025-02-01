
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 检查是否可以将二叉树分成两部分，使得每部分的节点值之和相等
    def checkEqualTree(self, root: TreeNode) -> bool:
        nodeSum = collections.defaultdict(int)
        
        # 深度优先搜索计算每个子树的总和，并记录在字典中
        def dfs(node):
            if not node:
                return 0
            sm = node.val + dfs(node.left) + dfs(node.right)
            nodeSum[sm] += 1
            return sm
        
        totalSum = dfs(root)
        
        # 如果总和为零，检查是否存在两个节点值之和为零的情况
        if not totalSum:
            return nodeSum[0] > 1
        
        # 检查总和是否能被2整除，并且半数的值在字典中存在
        return totalSum % 2 == 0 and totalSum // 2 in nodeSum

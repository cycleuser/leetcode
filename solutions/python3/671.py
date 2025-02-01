
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 寻找二叉树的第二小值
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # 初始化最小值为正无穷大
        self.sec = float('inf')

        # 深度优先搜索函数
        def dfs(node):
            if not node: 
                return
            # 递归遍历左右子树
            dfs(node.left)
            dfs(node.right)
            # 更新第二小值
            if root.val < node.val < self.sec:
                self.sec = node.val
        
        # 开始深度优先搜索
        dfs(root)

        # 如果没有找到更小的值，返回-1
        return self.sec if self.sec < float('inf') else -1

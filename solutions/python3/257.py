
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 找到二叉树的所有路径
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 深度优先搜索辅助函数
        def dfs(node, arr):
            if not node.right and not node.left:
                # 如果当前节点没有左右子节点，则记录一条完整路径
                self.res += ['->'.join(str(num) for num in arr)]
            if node.left:
                # 递归处理左子树
                dfs(node.left, arr + [node.left.val])
            if node.right:
                # 递归处理右子树
                dfs(node.right, arr + [node.right.val])
        
        self.res = []
        # 如果根节点为空，直接返回空列表
        if not root: return []
        # 开始深度优先搜索
        dfs(root, [root.val])
        # 返回所有路径的结果
        return self.res

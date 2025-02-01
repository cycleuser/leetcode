
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 计算二叉树中任意两个节点值之间的最大差值，其中较大的节点是较小节点的祖先
    def maxAncestorDiff(self, root: TreeNode) -> int:
        """
        :param root: 二叉树根节点
        :return: 二叉树中任意两个节点值之间的最大差值
        """

        self.res = 0
        
        # 深度优先搜索，计算当前节点的最大最小值，并更新结果
        def dfs(node):
            """
            :param node: 当前遍历到的节点
            :return: 以该节点为根的最大最小值
            """
            mx, mn = node.val, node.val
            
            if node.left:
                lMn, lMx = dfs(node.left)
                mx = max(mx, lMx)
                mn = min(mn, lMn)
                self.res = max(self.res, abs(lMn - node.val), abs(lMx - node.val))
                
            if node.right:
                rMn, rMx = dfs(node.right)
                mx = max(mx, rMx)
                mn = min(mn, rMn)
                self.res = max(self.res, abs(rMn - node.val), abs(rMx - node.val))
            
            return mn, mx
        
        dfs(root)  # 开始深度优先搜索
        return self.res  # 返回结果

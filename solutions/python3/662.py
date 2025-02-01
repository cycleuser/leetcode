
class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        英文注释：Given a binary tree, the function calculates and returns the maximum width of the tree. The width is defined as the largest number of nodes in any level of the tree.
        
        中文注释：给定一个二叉树，函数计算并返回该二叉树的最大宽度。宽度定义为树中任意一层的最大节点数。
        """
        dic, stack, res = {root: 1}, [root], 0
        # 使用广度优先搜索遍历整棵树
        while any(stack):
            tmp, mn, mx = [], float("inf"), -float("inf")
            for node in stack:
                # 更新当前层的最大宽度
                res = max(res, dic[stack[-1]] - dic[stack[0]] + 1)
                if node.left: 
                    tmp, dic[node.left] = tmp + [node.left], dic[node] * 2 - 1 
                if node.right:
                    tmp, dic[node.right] = tmp + [node.right], dic[node] * 2
            stack = tmp
        return res

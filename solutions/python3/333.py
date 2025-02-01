
class Solution:
    def largestBSTSubtree(self, root):
        """
        寻找二叉树中最大的BST子树的大小
        
        @param root: 二叉树的根节点
        """

        def dfs(node):
            """
            深度优先搜索，递归判断以当前节点为根的最大BST子树信息

            @param node: 当前处理的节点
            @return: 元组 (是否是BST, 节点数量, 最大值, 最小值, 大BST子树的大小)
            """
            if not node:
                # 空节点，视为BST，且节点数为0
                return True, 0, None, None, 0

            lBool, lSize, lMx, lMn, lTree = dfs(node.left)  # 左子树信息
            rBool, rSize, rMx, rMn, rTree = dfs(node.right)  # 右子树信息

            lVal = lMx if lMx is not None else -float("inf")  # 左子树的最大值
            rVal = rMn if rMn is not None else float("inf")   # 右子树的最小值

            curMx = max(val for val in (lMx, rMx, node.val) if val is not None)  # 当前节点的最大值
            curMn = min(val for val in (lMn, rMn, node.val) if val is not None)  # 当前节点的最小值

            curBool = lBool and rBool and lVal < node.val < rVal  # 判断当前子树是否为BST
            # 返回元组: 是否是BST，节点总数，当前最大值，当前最小值，当前子树中的最大BST大小
            return (
                curBool, 
                lSize + rSize + 1, 
                curMx, 
                curMn, 
                curBool and (lSize + rSize + 1) or max(lTree, rTree)
            )

        # 返回根节点的最大BST子树的大小
        return dfs(root)[4]

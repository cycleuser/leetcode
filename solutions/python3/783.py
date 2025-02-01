
class Solution:
    # 定义一个递归函数进行深度优先搜索，用于遍历二叉查找树的每个节点
    def minDiffInBST(self, root):
        # 递归终止条件：如果当前节点为空，则返回无穷大表示不存在差值，以及左右边界值
        def dfs(node):
            if not node:
                return float("inf"), float("inf"), -float("inf")
            
            # 对左子树进行递归调用，获取最小最大值和左右边界
            l, lMn, lMx = dfs(node.left)
            # 对右子树进行递归调用，获取最小最大值和左右边界
            r, rMn, rMx = dfs(node.right)

            # 计算当前节点与左子树的最大值的差值、当前节点与右子树的最小值的差值，以及左子树中的最小值、右子树中的最大值
            return min(l, node.val - lMx, r, rMn - node.val), min(lMn, node.val), max(rMx, node.val)
        
        # 调用dfs函数开始遍历，并返回二叉查找树中节点间最小差值
        return dfs(root)[0]

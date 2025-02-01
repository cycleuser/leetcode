
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 初始化结果为最大值
    res = sys.maxsize
    
    def getMinimumDifference(self, root: TreeNode) -> int:
        """
        :param root: 二叉树根节点
        :return: 二叉树任意两节点值之差的最小值
        """
        
        # 定义深度优先搜索函数，返回当前子树最大最小值
        def dfs(node):
            if not node:
                return sys.maxsize, -sys.maxsize
            
            # 对左子树递归调用dfs
            lMn, lMx = dfs(node.left)
            # 对右子树递归调用dfs
            rMn, rMx = dfs(node.right)
            
            # 更新最小差值
            self.res = min(self.res, node.val - lMx, rMn - node.val)
            
            # 返回当前节点的最小值和最大值
            return min(node.val, lMn), max(node.val, rMx)
        
        dfs(root)  # 调用dfs函数从根节点开始
        return self.res  # 返回最终结果

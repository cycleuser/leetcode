
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 寻找二叉树中最接近目标值的节点值
    # :type root: TreeNode 二叉树根节点
    # :type target: float 目标浮点数
    # :rtype: int 返回最接近目标值的整数值
    def closestValue(self, root, target):
        res, d = [0], [float("inf")]  # 初始化结果和最小差值
        
        def dfs(node):
            if node:
                new = abs(target - node.val)  # 计算当前节点与目标值的绝对差值
                if new < d[0]:
                    d[0] = new  # 更新最小差值
                    res[0] = node.val  # 更新结果
                if target < node.val:  # 如果目标值小于当前节点值，搜索左子树
                    dfs(node.left)
                else:
                    dfs(node.right)  # 否则搜索右子树

        dfs(root)  # 开始深度优先遍历
        return res[0]  # 返回最接近的节点值

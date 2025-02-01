
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    该类用于解决二叉树层次遍历的问题，目标是找到层次和最大的那一层。
    """

    def maxLevelSum(self, root: TreeNode) -> int:
        # 初始化层级列表、当前层数l和队列q
        levels, l, q = [], 1, [root]
        
        # 当队列不为空时进行循环
        while q:
            # 计算当前层节点值之和，并记录该层及其层级号
            levels.append([sum(node.val for node in q), l])
            
            # 层数加一
            l += 1
            
            # 更新队列为下一层的节点列表
            q = [child for node in q for child in (node.left, node.right) if child]
        
        # 对层级和进行排序，取最大值所在的层数
        return sorted(levels, key=lambda x: (x[0], -x[1]))[-1][1]

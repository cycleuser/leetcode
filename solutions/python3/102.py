
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 用于层次遍历二叉树并返回节点值的列表
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q, res = [root], []  # 初始化队列和结果列表
        while any(q):  # 队列非空时循环
            res.append([i.val for i in q])  # 将当前层节点值加入结果中
            q = [kid for node in q for kid in (node.left, node.right) if kid]  # 更新队列为下一层的节点
        return res  # 返回层次遍历的结果

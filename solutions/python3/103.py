
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 用于处理二叉树节点的层次遍历，返回按之字形顺序排列的结果
    # :type root: TreeNode 根节点
    # :rtype: List[List[int]] 按照之字形顺序的每一层节点值列表
    
    def zigzagLevelOrder(self, root):
        q, i, res = [root], 0, []
        
        while any(q):  # 当队列非空时循环
            if i % 2 == 0:  # 偶数层，直接添加
                add, q, i = q, [kid for node in q for kid in (node.left, node.right) if kid], i + 1
            else:  # 奇数层，倒序添加
                add, q, i = q[::-1], [kid for node in q for kid in (node.left, node.right) if kid], i + 1
            
            res.append([item.val for item in add])  # 将节点值加入结果列表
        
        return res

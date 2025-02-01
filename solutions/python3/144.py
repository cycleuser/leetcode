
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 先序遍历二叉树，返回节点值列表
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = [root]
        q = [root]
        
        # 当队列不为空时继续循环
        while any(q):
            tmp = []
            
            for node in q:
                if node.right:  # 如果右子节点存在，则插入当前节点右侧
                    res.insert(res.index(node) + 1, node.right)
                    tmp.append(node.right)
                
                if node.left:   # 如果左子节点存在，则插入当前节点左侧
                    res.insert(res.index(node) + 1, node.left)
                    tmp.insert(-1, node.left)
            
            q = tmp  # 更新队列为临时列表tmp

        return [j.val for j in res if j]  # 返回结果列表，过滤掉None值

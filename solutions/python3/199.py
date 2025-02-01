
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 右视图，返回二叉树的右视图中每个节点的值
    def rightSideView(self, root: 'TreeNode') -> 'List[int]':
        q, res = [root], []
        
        # 当队列不为空时继续遍历
        while any(q):
            # 将当前层最右边的节点值加入结果列表
            res.append(q[-1].val)
            
            # 生成下一层节点的列表，仅包含非空子节点
            q = [kid for node in q for kid in (node.left, node.right) if kid]
        
        return res

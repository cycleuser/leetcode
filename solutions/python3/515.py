
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Given the root of a binary tree, returns the largest values in each level.
    # 中文注释：给定一个二叉树的根节点，返回每一层中的最大值。
    
    def largestValues(self, root: TreeNode) -> List[int]:
        from collections import deque
        # 初始化队列和结果列表
        # 如果根节点为空，则直接返回空列表
        q, res = deque([root]) if root else None, [] if not root else [root.val]
        
        while q:
            node = q.popleft()
            if node.left: 
                q.append(node.left)
            if node.right: 
                q.append(node.right)
            
            # 当前节点是当前层最后一个节点，记录该层最大值
            if not q or node == target:
                res.append(max([i.val for i in q]))
                # 更新目标节点为下一层的最右节点
                if q: target = q[-1]
        
        return res

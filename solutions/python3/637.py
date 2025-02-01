
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: 'TreeNode') -> 'List[float]':
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import deque
        
        # 初始化队列和目标节点，记录每一层的平均值
        q, target, avg = deque([root]), root, [float(root.val)]
        
        while q:
            node = q.popleft()
            
            # 将左右子节点加入队列中
            if node.left: 
                q.append(node.left)
            if node.right: 
                q.append(node.right)
                
            # 当前层遍历结束时计算平均值
            if q and node == target:
                target, sm = q[-1], 0
                for item in q: 
                    sm += item.val
                avg.append(sm / len(q))
        
        return avg

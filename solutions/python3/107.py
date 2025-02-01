
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    该类用于实现二叉树的层次遍历（从底到顶）
    
    Attributes:
        - root: 树的根节点
    """
    def levelOrderBottom(self, root):
        """
        使用广度优先搜索实现二叉树的层次遍历，并将结果逆序返回
        
        Args:
            :type root: TreeNode 根节点

        Returns:
            List[List[int]] 返回从底到顶每层结点值组成的二维列表
        """
        from collections import deque
        if root is None:
            return []
        
        # 用于存储每一层的节点值
        levels = list()
        # 队列，初始化时加入根节点
        q = deque([root])
        
        # 将第一层的节点值添加到levels中
        levels.append([i.val for i in q])

        # 使用目标节点target来指示当前层的最后一个结点
        target = root
        
        while q:
            node = q.popleft()
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            # 如果当前处理的是该层的最后一个结点，将其右子节点加入levels中
            if node == target and q:
                levels.append([i.val for i in q])
                target = q[-1]

        return list(reversed(levels))

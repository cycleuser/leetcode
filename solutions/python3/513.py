
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 寻找二叉树最底层最左边的节点值
    # Find the leftmost value in the last level of a binary tree
    
    def findBottomLeftValue(self, root: TreeNode) -> int:
        bfs = [root]
        
        while bfs:
            # 在每一层中，左节点的值即为该层最左侧节点的值
            # At each level, the leftmost node's value is the leftmost value of that level
            left = bfs[0].val
            
            # 使用列表生成式遍历当前层的所有子节点，并添加到队列中
            # Traverse all children nodes of current level and add them to the queue
            bfs = [child for node in bfs for child in (node.left, node.right) if child]
        
        return left

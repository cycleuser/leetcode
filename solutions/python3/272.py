
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 寻找二叉树中与目标值最接近的k个节点
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[float]:
        d = []
        
        # 深度优先搜索遍历二叉树，并维护一个最小堆，记录每个节点与其目标值的差值和节点值
        def dfs(node):
            if node:
                heapq.heappush(d, (abs(node.val - target), node.val))
                dfs(node.left)
                dfs(node.right)
        
        # 开始遍历二叉树
        dfs(root)
        
        # 从最小堆中取出k个最接近目标值的节点值
        return [node for val, node in heapq.nsmallest(k, d)]

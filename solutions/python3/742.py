
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    定义一个Solution类来解决寻找最接近叶子节点的问题。
    
    解题思路：使用深度优先搜索（DFS）构建图结构，然后使用广度优先搜索（BFS）从k开始寻找最近的叶子结点。
    """

    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        # 使用defaultdict存储节点之间的邻接关系
        adj = collections.defaultdict(list)
        q = []  # 初始化队列用于BFS遍历
        visited = collections.defaultdict(int)  # 记录已经访问过的节点

        def dfs(node):
            """
            深度优先搜索构建图结构，从root开始。
            如果遇到目标节点k，将其加入队列q，并标记为已访问；对于每个子节点，建立双向连接并递归处理。
            """
            if node:
                if node.val == k:
                    q.append(node)
                    visited[node.val] = 1
                if node.left:
                    adj[node].append(node.left)
                    adj[node.left].append(node)
                    dfs(node.left)
                if node.right:
                    adj[node].append(node.right)
                    adj[node.right].append(node)
                    dfs(node.right)

        # 调用DFS初始化图结构
        dfs(root)

        while q:
            new = []
            for node in q:
                # 如果当前节点是叶子节点，直接返回其值
                if not node.left and not node.right:
                    return node.val
                # 遍历邻接表中的所有连接节点
                for v in adj[node]:
                    if not visited[v.val]:
                        visited[v.val] = 1
                        new.append(v)
            q = new  # 更新队列

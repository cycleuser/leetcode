
class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        """
        复制给定的图结构。使用深度优先搜索（DFS）来确保所有节点都被正确复制。

        参数：
            node (Node): 起始节点

        返回值：
            Node: 新复制的图
        """
        visited = {}

        def dfs(node):
            """
            深度优先搜索函数，用于递归地创建新节点及其邻居。
            
            参数：
                node (Node): 当前处理的节点

            返回值：
                Node: 复制的新节点
            """
            if node and node.val not in visited:
                # 创建一个新的节点，并记录其值
                newNode = Node(node.val, [])
                visited[newNode.val] = newNode
                # 递归地为当前节点的所有邻居创建新节点，并设置邻居列表
                newNode.neighbors = [
                    visited.get(n.val) or dfs(n) for n in node.neighbors
                ]
                return newNode

        return dfs(node)

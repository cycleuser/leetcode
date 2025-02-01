
class Solution:
    # 初始化邻接表，结果集和访问状态标记
    def distanceK(self, root, target, K):
        adj, res, visited = collections.defaultdict(list), [], collections.defaultdict(int)

        # 构建邻接表
        def dfs(node):
            if node.left:  # 如果当前节点有左子节点
                adj[node].append(node.left)  # 将节点与左子节点相连
                adj[node.left].append(node)  # 并将左子节点与当前节点相连
                dfs(node.left)  # 继续递归遍历左子树

            if node.right:  # 如果当前节点有右子节点
                adj[node].append(node.right)  # 将节点与右子节点相连
                adj[node.right].append(node)  # 并将右子节点与当前节点相连
                dfs(node.right)  # 继续递归遍历右子树

        dfs(root)

        # 深度优先搜索，查找距离目标节点K步的节点
        def dfs2(node, d):
            if d < K:  # 如果当前深度小于K
                visited[node] = 1  # 标记该节点为已访问
                for v in adj[node]:  # 遍历所有邻接节点
                    if not visited[v]:  # 如果该邻接节点未被访问过
                        dfs2(v, d + 1)  # 继续递归查找

                visited[node] = 0  # 查找结束后，标记该节点为未访问（已出栈）

            else:
                res.append(node.val)  # 当前深度等于K时，将当前节点值加入结果集

        dfs2(target, 0)  # 从目标节点开始查找
        return res

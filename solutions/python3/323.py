
class Solution:
    # 定义一个类用于求解图的连通分量数量

    def countComponents(self, n: int, edges: List[Tuple[int, int]]) -> int:
        # 初始化已访问集合、结果计数器和邻接表
        visited, res, adj = set(), 0, collections.defaultdict(set)
        
        # 构建图的邻接表表示
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        # 深度优先搜索函数，用于遍历连通分量
        def dfs(i):
            visited.add(i)
            for v in adj[i]:
                if v not in visited:
                    dfs(v)
        
        # 遍历所有节点，统计连通分量数量
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)

        return res

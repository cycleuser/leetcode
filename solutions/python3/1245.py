
class Solution:
    # 计算树的最大直径
    def treeDiameter(self, edges: List[List[int]], move: int = 0) -> int:
        # 构建无向图的邻接表表示
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        # 初始化bfs集合，包含所有度为1的节点及其父节点
        bfs = {(u, None) for u, nex in graph.items() if len(nex) == 1}

        # 进行广度优先搜索，逐步扩展到最远端点
        while bfs:
            bfs, move = (
                {(v, u) for u, pre in bfs for v in graph[u] if v != pre},  # 更新bfs集合为下一层节点
                move + 1,  # 深度加一
            )

        # 返回最大深度减1作为直径（树的直径等于最远两点间的距离）
        return max(move - 1, 0)

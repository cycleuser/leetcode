
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        判断从source出发是否可以到达destination，且路径上不能有环。

        中文解释：判断从给定起点到终点是否存在一条路径，并确保这条路径是有效的（即没有形成环）。
        """

        def dfs(i):
            """
            深度优先搜索函数

            参数：
                i (int): 当前节点的索引
            返回：
                bool: 是否存在从i出发能到达destination且不形成环的路径
            """
            seen.add(i)
            for j in graph[i]:
                if j == i or j in seen or not dfs(j):
                    return False
            seen.discard(i)
            # 如果当前节点没有出边，或者该节点就是目的地，则返回True
            return len(graph[i]) != 0 or i == destination

        graph, seen = collections.defaultdict(set), set()
        for a, b in edges:
            graph[a].add(b)
        return dfs(source)

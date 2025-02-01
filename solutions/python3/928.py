
class Solution:
    def minMalwareSpread(self, graph, initial):
        """
        寻找最小化感染范围的初始节点
        
        参数：
        graph：邻接矩阵表示的图结构
        initial：初始被感染节点列表

        返回值：
        最小化感染范围的初始节点
        """

        def dfs(i):
            """
            深度优先搜索查找与i相连且未访问过的节点
            
            参数：
            i：当前节点索引
            
            返回值：
            True或False，表示是否有新的连接且未被访问过
            """
            seen.add(i)
            return not any(graph[i][j] and j not in seen and (j in initials or not dfs(j)) for j in range(len(graph[i])))

        res, mx, initials = min(initial), 1, set(initial)  # 初始结果，最大影响节点数，初始感染节点集合
        for node in sorted(initial):  # 遍历所有初始感染节点
            impact = set()  # 影响节点集

            for j in range(len(graph[node])):  # 遍历当前节点的所有邻接节点
                seen = {node}  # 当前访问集合初始化为当前节点
                if graph[node][j] and j not in initials and dfs(j):  # 如果节点j满足条件，进行DFS并更新影响集
                    impact |= seen

            if len(impact) > mx:  # 更新结果
                res, mx = node, len(impact)

        return res

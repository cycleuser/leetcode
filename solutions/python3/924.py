
class Solution:
    # 定义一个解题类

    def minMalwareSpread(self, graph, initial):
        """
        :param graph: 二维列表，表示图的连接关系
        :param initial: 列表，初始被感染节点的集合
        :return: 返回最小蔓延点，使得仅该节点被移除后能减少最多感染节点
        """

        def dfs(i):
            # 深度优先搜索函数
            nodes.add(i)
            for j in range(len(graph[i])):
                if graph[i][j] and j not in nodes:
                    dfs(j)

        rank, initial_set = collections.defaultdict(list), set(initial)
        # 初始化排名字典和初始感染节点集合

        for node in sorted(initial_set):
            # 遍历排序后的初始感染节点
            nodes = set()
            dfs(node)
            # 对每个节点进行深度优先搜索并记录其连接节点集
            if nodes & initial_set == {node}:
                # 检查当前节点是否是唯一的初始感染节点
                rank[len(nodes)].append(node)

        return rank[max(rank)][0] if rank else min(initial_set)
        # 返回排名最高的唯一感染节点，或者如果没有满足条件的节点，则返回最小的初始感染节点

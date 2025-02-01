
from collections import defaultdict

class Solution:
    def reachableNodes(self, edges, M, N):
        """
        生成图的邻接表表示，并初始化已访问节点集合。
        
        :param edges: 列表，包含边及其对应的长度
        :param M: 源点可以移动的最大步数
        :param N: 节点总数（虽然未直接使用）
        :return: 可达节点对的总和 + 已访问节点数量
        """
        # 使用defaultdict来存储图的邻接表表示，并初始化已访问节点集合
        adj, seen = defaultdict(dict), set()
        
        # 遍历每条边，填充邻接表并记录初始步数为0
        for a, b, l in edges:
            adj[a][b] = [l, 0]
            adj[b][a] = [l, 0]

        q = [(0, M, None)]
        
        # 使用广度优先搜索更新每条边的可到达步数上限
        while q:
            new = []
            for i, moves, pre in q:
                seen.add(i)
                for j in adj[i]:
                    if moves > adj[i][j][1]:
                        adj[i][j][1] = moves
                        # 如果当前节点可以访问到的步数大于初始步数，并且不是前一个节点，则添加新的队列元素
                        if moves > adj[i][j][0] and j != pre:
                            new.append((j, moves - adj[i][j][0] - 1, i))
            q = new

        # 计算可达节点对的总和以及已访问节点数量
        return sum(min(adj[i][j][1] + adj[j][i][1], l) for i, j, l in edges) + len(seen)

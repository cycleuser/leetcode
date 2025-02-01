
class Solution:
    def findRedundantDirectedConnection(self, edges):
        # 获取节点的根节点
        def root(i):
            return parent[i] if parent[i] == i else root(parent[i])
        
        # 初始化父节点数组、候选A、B和C边
        parent, a, b, c = [0] * (len(edges) + 1), None, None, None
        
        for i, edge in enumerate(edges):
            if parent[edge[1]]:
                # 如果已有指向edge[1]的父节点，记录为候选A、B和C边
                a, b, c, edges[i][0] = parent[edge[1]], edge[0], edge[1], 0
            else:
                # 否则设置新的指向关系
                parent[edge[1]] = edge[0]
        
        # 重置父节点数组，初始化为节点索引
        parent = [i for i in range(len(edges) + 1)]
        
        # 构建有向图并寻找冗余边
        for u, v in edges:
            if u:
                if root(u) == v: 
                    return a and [a, c] or [u, v]
                parent[v] = u   
        return [b, c]

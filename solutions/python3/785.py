
class Solution:
    # 定义判断图是否为二分图的方法
    def isBipartite(self, graph):
        # 初始化每个节点所属的"侧"，0表示未访问
        side = [0] * len(graph)
        
        # 深度优先搜索辅助函数
        def dfs(node):
            # 遍历当前节点的所有邻接节点
            for v in graph[node]:
                if side[v] == 0: 
                    # 如果未被访问，分配不同的"侧"
                    side[v] = -side[node]
                    # 继续递归检查该邻接节点
                    if not dfs(v):
                        return False
                elif side[v] == side[node]: 
                    # 若邻接节点与当前节点同"侧"，返回False
                    return False
            return True
        
        # 遍历图中每个节点
        for i in range(len(graph)):
            # 如果未被访问，则标记为1并进行深度优先搜索
            if side[i] == 0: 
                side[i] = 1
            if not dfs(i):
                return False
        
        return True

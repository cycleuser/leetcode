
class Solution:
    def allPathsSourceTarget(self, graph, i=0, q=[0]):
        """
        :param graph: 邻接表表示的图 (graph)
        :param i: 当前处理节点索引 (i)
        :param q: 从源点到当前节点的路径列表 (q)
        :return: 所有可能的从源点到目标点的路径列表 (res)
        """
        
        if i == 0:
            # 如果是起始节点，初始化结果列表
            self.res = []
            
        if i == len(graph) - 1:
            # 当到达目标节点时，将当前路径添加到结果中
            self.res.append(q)
            
        for index in graph[i]:
            # 对于当前节点的所有邻居，递归寻找路径
            self.allPathsSourceTarget(graph, index, q + [index])
        
        return self.res

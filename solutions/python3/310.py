
class Solution:
    # 寻找具有最小高度的树根节点
    def findMinHeightTrees(self, n, edges):
        """
        :param n: 图中的节点数 (int)
        :param edges: 表示图中边的列表，每个元素是一个长度为2的元组 (List[List[int]])
        :return: 具有最小高度的树根节点的索引列表 (List[int])
        """

        if n == 1:
            # 如果只有一个节点，则返回该节点
            return [0]

        # 构建邻接表表示图
        adj = [set() for i in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        # 找出所有叶子节点（度为1的节点）
        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            # 更新节点数量
            n -= len(leaves)
            newleaves = []
            
            # 移除叶子节点并更新邻接表
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newleaves.append(j)

            leaves = newleaves

        return leaves

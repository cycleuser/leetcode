
class Solution:
    # 定义并查集类
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 初始化parent数组，用于记录每个节点的父节点
        parent = [0] * len(edges)

        # 查找操作：找到某个节点的根节点
        def find(x):
            if parent[x] == 0:
                return x
            # 路径压缩优化
            parent[x] = find(parent[x])
            return parent[x]

        # 合并操作：将两个集合合并，返回是否成功
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            # 将x的根节点指向y的根节点
            parent[rootX] = rootY
            return True

        res = [0, 0]
        for x, y in edges:
            # 如果合并失败，说明存在冗余连接
            if not union(x - 1, y - 1):
                res = [x, y]
        return res

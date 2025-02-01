
class Solution:
    # 定义一个解决方案类

    def minCostToSupplyWater(self, n: int, wells, pipes) -> int:
        # 将管道成本按升序排序，并将水井的成本添加到排序中，每个水井看作是从虚拟节点0连向其编号的边
        q = sorted([[w, u, v] for u, v, w in pipes] + [[w, 0, i+1] for i, w in enumerate(wells)])
        
        # 初始化并查集
        uf = [i for i in range(n+1)]
        res = count = 0
        
        # 并查集查找函数，返回节点的根，并进行路径压缩
        def find(x):
            if (x != uf[x]):
                uf[x] = find(uf[x])
            return uf[x]
        
        # 并查集合并函数，将两个集合合并
        def union(x, y):
            uf[x] = y
            
        # 遍历排序后的边，构建最小生成树
        for w, u, v in q:
            rA, rB = find(u), find(v)
            if rA == rB:
                continue  # 如果两个节点已经属于同一个集合，则跳过这次操作
            union(rA, rB)  # 否则，合并这两个节点所在的集合，并将成本累加到结果中
            res += w
            count += 1
            if count == n:  # 当构建的生成树包含所有n个节点时，返回最终的成本
                return res
        return res  # 如果未形成完整的生成树，则返回当前累加的结果

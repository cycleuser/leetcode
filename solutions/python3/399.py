
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        计算给定方程组的比值。
        
        参数:
            equations (List[Tuple[str, str]]): 方程对列表，每个元素为一个元组表示两个变量之间的关系。
            values (List[float]): 每个方程对应的比值。
            queries (List[Tuple[str, str]]): 需要查询的变量对。

        返回:
            List[float]: 各个查询结果，如果不存在则返回-1.0。
        """

        def explore(x, y, r, q):
            """
            递归查找两个节点之间的比值关系。

            参数:
                x (str): 起始节点。
                y (str): 目标节点。
                r (float): 当前路径的乘积结果。
                q (set[str]): 已访问过的节点集合，避免重复计算。
            """
            results[(x, y)] = r
            for z in edges[y]:
                if z not in q:
                    results[(x, z)], results[(z, x)] = r * vals[(y, z)], 1 / (r * vals[(y, z)])
                    explore(x, z, r * vals[(y, z)], q | {z})

        # 边集合
        edges = collections.defaultdict(set)
        # 比值字典
        vals = {}
        # 已访问的节点集合
        visited = set()
        # 查询结果存储
        results = {}
        res = []

        # 构建图结构
        for i, eq in enumerate(equations):
            edges[eq[0]].add(eq[1])
            edges[eq[1]].add(eq[0])
            vals[(eq[0], eq[1])], vals[(eq[1], eq[0])] = values[i], 1 / values[i]

        # 遍历每个方程中的变量
        for i, eq in enumerate(equations):
            for p in eq:
                if p not in visited:
                    visited.add(p)
                    explore(p, p, 1.0, {p})

        # 查询处理
        for q in queries:
            if (q[0], q[1]) in results: 
                res += [results[(q[0], q[1])]]
            else: 
                res += [-1.0]

        return res

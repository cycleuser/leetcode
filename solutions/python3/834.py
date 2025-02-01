
class Solution:
    # 初始化树和结果列表，每个节点的子节点计数以及路径长度
    def sumOfDistancesInTree(self, N: int, edges: list[list[int]]) -> list[int]:
        from collections import defaultdict

        tree = defaultdict(set)  # 存储树结构，默认值为集合
        res = [0] * N  # 初始化结果列表，每个节点的路径长度初始化为0
        count = [1] * N  # 初始化子节点计数，每个节点初始子节点数为1

        for i, j in edges:
            tree[i].add(j)  # 构建树结构
            tree[j].add(i)

        def dfs(root: int, pre: int) -> None:
            """深度优先搜索计算每个节点的路径长度和子节点计数"""
            for i in tree[root]:
                if i != pre:
                    dfs(i, root)  # 递归遍历子节点
                    count[root] += count[i]  # 更新当前节点的子节点总数
                    res[root] += res[i] + count[i]  # 更新当前节点路径长度

        def dfs2(root: int, pre: int) -> None:
            """第二次深度优先搜索，计算每个节点相对于根节点的路径长度"""
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + N - count[i]  # 计算新路径长度
                    dfs2(i, root)  # 递归遍历子节点

        dfs(0, -1)  # 从根节点开始，深度优先搜索计算初始路径长度和子节点数
        dfs2(0, -1)  # 再次深度优先搜索，计算最终每个节点的路径长度
        
        return res  # 返回结果列表

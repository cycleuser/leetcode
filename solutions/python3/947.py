
class Solution:
    def removeStones(self, stones):
        """
        移除石子问题：计算能够通过移除最少数量的石子，使剩余石子分布在多个独立岛上的数量。

        Args:
            stones (List[Tuple[int, int]]): 石子的位置列表

        Returns:
            int: 需要移除的最小石子数
        """

        def dfs(i, j):
            """
            深度优先搜索遍历当前岛屿的所有连通石子。

            Args:
                i (int): 当前行号
                j (int): 当前列号
            """
            points.discard((i, j))
            for y in rows[i]:
                if (i, y) in points:
                    dfs(i, y)
            for x in cols[j]:
                if (x, j) in points:
                    dfs(x, j)

        # 初始化数据结构
        points, island, rows, cols = {(i, j) for i, j in stones}, 0, collections.defaultdict(list), collections.defaultdict(list)
        
        # 构建行和列的索引
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)

        # 遍历石子进行DFS，计算独立岛的数量
        for i, j in stones:
            if (i, j) in points:
                dfs(i, j)
                island += 1

        return len(stones) - island

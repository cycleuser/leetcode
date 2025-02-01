
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        初始化网格的行数和列数，以及起始步长d。
        使用defaultdict存储每个空地被哪些源点可达及其累积距离。
        找到所有源点（值为1的位置）并初始化队列bfs。
        总共有total个源点，res用于存储最短距离结果列表。
        """
        m, n, d = len(grid), len(grid[0]), 1
        piled = collections.defaultdict(set)
        dist = collections.defaultdict(int)
        
        bfs = [(i, j, i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        total, res = len(bfs), []

        while bfs:
            """
            每次遍历，记录新的bfs队列new。
            对于当前层的所有点(x, y)，检查其四个方向上的邻点(ii, jj)：
                - 如果是有效空地且未被当前源点访问过，则标记此访问并更新距离；
                - 当该空地被所有源点可达时，将其距离加入结果列表。
            更新bfs为new，并增加步长d。
            """
            new = []
            for x, y, i, j in bfs:
                for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= ii < m and 0 <= jj < n and not grid[ii][jj] and (x, y) not in piled[(ii, jj)]:
                        piled[(ii, jj)].add((x, y))
                        dist[(ii, jj)] += d
                        if len(piled[(ii, jj)]) == total:
                            res.append(dist[(ii, jj)])
                        new.append((x, y, ii, jj))
            bfs = new
            d += 1
        
        """
        返回最短距离，若无有效结果则返回-1。
        """
        return min(res) if res else -1


class Solution:
    def largestIsland(self, grid):
        """
        解决问题：找出给定二维网格中最大岛屿的面积。
        
        参数：
            - grid: List[List[int]] -- 给定的0（水）和1（陆地）构成的矩阵
        
        返回值：
            - int -- 最大的岛屿面积
        """
        
        def explore(i, j):
            """
            递归遍历岛屿，并标记访问过的节点。
            
            参数：
                - i: int -- 当前行索引
                - j: int -- 当前列索引
            """
            dic[(i, j)], count[curr] = curr, count[curr] + 1
            if i > 0 and grid[i - 1][j] == 1 and (i - 1, j) not in dic:
                explore(i - 1, j)
            if j > 0 and grid[i][j - 1] == 1 and (i, j - 1) not in dic:
                explore(i, j - 1)
            if i + 1 < len(grid) and grid[i + 1][j] == 1 and (i + 1, j) not in dic:
                explore(i + 1, j)
            if j + 1 < len(grid) and grid[i][j + 1] == 1 and (i, j + 1) not in dic:
                explore(i, j + 1)

        def neighbours(i, j, adj):
            """
            获取相邻的岛屿编号。
            
            参数：
                - i: int -- 当前行索引
                - j: int -- 当前列索引
                - adj: set[int] -- 存储相邻岛屿编号
            
            返回值：
                - adj: set[int] -- 更新后的相邻岛屿编号集合
            """
            if i > 0 and grid[i - 1][j] == 1 and dic[(i - 1, j)] not in adj:
                adj.add(dic[(i - 1, j)])
            if j > 0 and grid[i][j - 1] == 1 and dic[(i, j - 1)] not in adj:
                adj.add(dic[(i, j - 1)])
            if i + 1 < len(grid) and grid[i + 1][j] == 1 and dic[(i + 1, j)] not in adj:
                adj.add(dic[(i + 1, j)])
            if j + 1 < len(grid) and grid[i][j + 1] == 1 and dic[(i, j + 1)] not in adj:
                adj.add(dic[(i, j + 1)])
            return adj

        curr, dic, count, res = 0, {}, collections.defaultdict(int), 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1 and (i, j) not in dic:
                    curr += 1; explore(i, j)
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1: 
                    res = max(res, count[dic[(i, j)]])
                else:
                    adj = set()
                    res = max(res, sum(count[r] for r in neighbours(i, j, adj)) + 1)
        
        return res

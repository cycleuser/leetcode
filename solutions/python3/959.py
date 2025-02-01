
class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        """
        计算由网格中的斜杠和空格划分的区域数量。
        
        参数：
            grid：一个二维字符串列表，其中'\\'表示斜线，'/'表示反斜线，' '为空格。
        
        返回值：
            区域的数量。
        """

        def dfs(i: int, j: int, k: int) -> None:
            """
            深度优先搜索函数。

            参数：
                i：当前行索引
                j：当前列索引
                k：当前方向，0-左，1-右，2-下，3-上。
            """
            if 0 <= i < n and 0 <= j < n and not matrix[i][j][k]:
                # 根据字符类型进行分支处理
                match grid[i][j]:
                    case '\\':
                        if k == 1 or k == 2:
                            matrix[i][j] = [cnt, cnt]
                            dfs(i, j + 1, 3)
                            dfs(i + 1, j, 0)
                        else:
                            matrix[i][j] = [cnt, cnt]
                            dfs(i - 1, j, 2)
                            dfs(i, j - 1, 1)
                    case '/':
                        if k == 0 or k == 3:
                            matrix[i][j] = [cnt, cnt]
                            dfs(i, j + 1, 3)
                            dfs(i + 1, j, 0)
                        else:
                            matrix[i][j] = [cnt, cnt]
                            dfs(i - 1, j, 2)
                            dfs(i, j - 1, 1)
                    case _:
                        matrix[i][j] = [cnt, cnt, cnt, cnt]
                        dfs(i - 1, j, 2)
                        dfs(i, j + 1, 3)
                        dfs(i + 1, j, 0)
                        dfs(i, j - 1, 1)

        # 替换双反斜线为星号
        grid = [row.replace("\\\\", "*") for row in grid]
        n = len(grid)
        matrix = [[[0] * 4 for _ in range(n)] for _ in range(n)]
        cnt = 0

        # 初始化矩阵并进行DFS遍历
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    if not matrix[i][j][k]:
                        cnt += 1
                        dfs(i, j, k)
        
        return cnt

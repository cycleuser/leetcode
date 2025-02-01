
class Solution:
    # 定义深度优先搜索函数，用于标记陆地并将相邻的'1'加入队列
    def dfs(self, i: int, j: int):
        A[i][j] = -1
        self.q.append((i, j))
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                self.dfs(x, y)

    # 定义寻找第一个陆地的辅助函数
    def first(self):
        for i in range(n):
            for j in range(n):
                if A[i][j]:
                    return i, j

    n, step, q = len(A), 0, []  # 初始化：岛屿个数、步数和队列
    self.dfs(*self.first())  # 从第一个陆地开始深度优先搜索

    while True:
        new = []
        for i, j in self.q:  # 遍历当前层的每个位置
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):  # 检查相邻的位置
                if 0 <= x < n and 0 <= y < n:
                    if A[x][y] == 1:  # 找到另一个岛屿，直接返回步数
                        return self.step
                    elif not A[x][y]:  # 将未访问过的陆地标记为已访问并加入下一层队列
                        A[x][y] = -1
                        new.append((x, y))
        self.step += 1  # 更新步数
        self.q = new  # 更新当前层的队列为下一层的队列

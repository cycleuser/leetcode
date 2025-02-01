
class Solution:
    # 初始化类，定义寻找所有钥匙的最短路径问题
    def shortestPathAllKeys(self, grid):
        final, m, n, si, sj = 0, len(grid), len(grid[0]), 0, 0
        # 遍历网格，计算最终需要收集的所有钥匙的状态，并找到起始点的位置
        for i in range(m):
            for j in range(n):
                if grid[i][j] in "abcdef":
                    final |= 1 << ord(grid[i][j]) - ord("a")
                elif grid[i][j] == "@":
                    si, sj = i, j

        q, memo = [(0, si, sj, 0)], set()
        # 使用优先队列进行广度优先搜索，同时记录已访问的状态
        while q:
            moves, i, j, state = heapq.heappop(q)
            if state == final: return moves
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                # 检查下一个位置是否在网格范围内且不是墙壁
                if 0 <= x < m and 0 <= y < n and grid[x][y] != "#":
                    # 如果遇到大写字母钥匙，检查对应的小写状态是否已收集
                    if grid[x][y].isupper() and not state & 1 << (ord(grid[x][y].lower()) - ord("a")): 
                        continue
                    # 更新状态：如果当前位置是小写字母钥匙，则更新state状态；否则保持不变
                    newState = ord(grid[x][y]) >= ord("a") and state | 1 << (ord(grid[x][y]) - ord("a")) or state
                    if (newState, x, y) not in memo:
                        memo.add((newState, x, y))
                        heapq.heappush(q, (moves + 1, x, y, newState))
        return -1

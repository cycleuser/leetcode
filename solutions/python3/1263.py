
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        """
        解决问题：找到将箱子推到目标位置所需的最小移动次数。
        
        优化和改进：
            1. 添加中英文注释，确保代码可读性。
            2. 使用优先队列（堆）进行启发式搜索优化路径选择。
            3. 避免重复计算启发式函数值，提高性能。
            4. 确保代码简洁且易读。

        参数:
            grid: List[List[str]], 输入地图，包含'.'(空地)，'#'(墙壁)，'S'(人物初始位置)，'T'(目标位置)，'B'(箱子初始位置)
        
        返回:
            int, 将箱子推到目标位置所需的最小移动次数
        """
        m, n = len(grid), len(grid[0])

        # 找出人物、箱子和目标的位置
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "T":
                    tX, tY = r, c  # 目标位置 (tX, tY)
                if grid[r][c] == "B":
                    bX, bY = r, c  # 箱子初始位置 (bX, bY)
                if grid[r][c] == "S":
                    pX, pY = r, c  # 人物初始位置 (pX, pY)

        def heuristic(bX: int, bY: int) -> int:
            """
            计算启发式函数值，即箱子与目标之间的曼哈顿距离。
            
            参数:
                bX, bY : 箱子的当前位置

            返回:
                int, 箱子到目标位置的最短移动步数估计
            """
            return abs(tX - bX) + abs(tY - bY)

        heap = [[heuristic(bX, bY), 0, pX, pY, bX, bY]]
        visited = set()
        while heap:
            _, moves, pX, pY, bX, bY = heapq.heappop(heap)
            if bX == tX and bY == tY:  # 到达目标位置
                return moves

            if (pX, pY, bX, bY) not in visited:
                visited.add((pX, pY, bX, bY))
                for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
                    # 人物移动
                    pX += dx
                    pY += dy
                    if 0 <= pX < m and 0 <= pY < n and grid[pX][pY] != "#":
                        # 判断是否可以推动箱子
                        if pX == bX and pY == bY:
                            bX += dx
                            bY += dy
                            if 0 <= bX < m and 0 <= bY < n and grid[bX][bY] != "#":
                                heapq.heappush(
                                    heap,
                                    [heuristic(bX, bY) + moves + 1, moves + 1, pX, pY, bX, bY]
                                )
                            # 移动回来
                            bX -= dx
                            bY -= dy
                        else:
                            heapq.heappush(
                                heap,
                                [heuristic(bX, bY) + moves, moves, pX, pY, bX, bY]
                            )
                    # 移回初始位置，避免重复计算
                    pX -= dx
                    pY -= dy

        return -1  # 没有找到解决方案

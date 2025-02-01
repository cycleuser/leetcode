
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # 初始化起始位置和移动次数，网格大小，已访问状态集合
        q, move, n, seen = {(0, 1, 0)}, 0, len(grid), set()
        
        while q:
            # 创建一个新的集合来存放下一轮可到达的位置
            new = set()
            
            for i, j, hv in q:
                # 到达终点且未水平移动过
                if i == j == n - 1 and not hv:
                    return move
                
                # 水平移动条件：下一行无障碍物
                if hv and i < n - 1 and not grid[i + 1][j]:
                    if (i + 1, j, 1) not in seen:
                        new.add((i + 1, j, 1))
                
                # 水平移动条件：右侧相邻格子无障碍物
                if hv and j + 1 < n and grid[i][j + 1] == grid[i - 1][j + 1] == 0:
                    if (i, j + 1, 1) not in seen:
                        new.add((i, j + 1, 1))
                    if (i - 1, j + 1, 0) not in seen:
                        new.add((i - 1, j + 1, 0))
                
                # 竖直移动条件：右侧无障碍物
                if not hv and j + 1 < n and not grid[i][j + 1]:
                    if (i, j + 1, 0) not in seen:
                        new.add((i, j + 1, 0))
                
                # 竖直移动条件：下一行相邻格子无障碍物
                if not hv and i + 1 < n and grid[i + 1][j] == grid[i + 1][j - 1] == 0:
                    if (i + 1, j, 0) not in seen:
                        new.add((i + 1, j, 0))
                    if (i + 1, j - 1, 1) not in seen:
                        new.add((i + 1, j - 1, 1))
            
            # 更新当前队列和已访问状态
            q = new
            seen |= new
            
            move += 1
        
        return -1

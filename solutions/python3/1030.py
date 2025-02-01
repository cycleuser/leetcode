
class Solution:
    # Python 解决方案类

    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # 初始化队列、结果列表和已访问集合
        bfs, res, seen = [[r0, c0]], [], {(r0, c0)}
        
        while bfs:
            # 将当前层节点添加到结果中
            res += bfs
            # 初始化新一层的节点列表
            new = []
            
            for i, j in bfs:
                # 遍历当前层节点的四个方向
                for x, y in (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1):
                    # 检查新坐标是否在范围内且未被访问过
                    if 0 <= x < R and 0 <= y < C and (x, y) not in seen:
                        seen.add((x, y))
                        new.append([x, y])
            
            bfs = new
        
        return res

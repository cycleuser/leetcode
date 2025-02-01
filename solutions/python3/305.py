
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[Tuple[int, int]]) -> List[int]:
        # 获取父节点，路径压缩优化
        def getParent(i):
            if i != parent[i]:
                parent[i] = getParent(parent[i])
            return parent[i]
        
        islands, res, parent, Id = set(), [], {}, 1
        
        for i, j in positions:
            # 添加新陆地并初始化其父节点
            parent[(i, j)] = parent[Id] = Id
            
            # 遍历四个方向，合并相邻陆地
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if (x, y) in parent:
                    p = getParent(parent[(x, y)])
                    islands.discard(p)
                    parent[p] = Id
            
            # 添加新的岛屿标识
            islands.add(Id)
            Id += 1
            
            # 更新结果集
            res.append(len(islands))
        
        return res

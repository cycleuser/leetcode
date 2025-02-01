
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        # 深度优先搜索，从当前节点i和颜色标记mod出发进行搜索
        # mod 0 表示红色边，1表示蓝色边
        def dfs(i, mod, cnt):
            res[i][mod] = cnt
            for v in edge[i][mod]:
                if cnt < res[v][1 - mod]:
                    dfs(v, 1 - mod, cnt + 1)
                    
        # 初始化结果数组和邻接表
        res = [[float('inf'), float('inf')] for _ in range(n)]
        edge = [[[], []] for _ in range(n)]
        
        # 填充红色边的邻接表
        for u, v in red_edges:
            edge[u][0].append(v)
            
        # 填充蓝色边的邻接表
        for u, v in blue_edges:
            edge[u][1].append(v)
        
        # 从起始节点进行两次深度优先搜索，一次红色起点，一次蓝色起点
        dfs(0, 0, 0)
        dfs(0, 1, 0)
        
        # 返回结果数组中最小值或-1（表示不可达）
        return [x if x != float('inf') else -1 for x in map(min, res)]


class Solution:
    # 判断给定的边集是否构成一棵有效的树
    
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        visited, adj = [0] * n, collections.defaultdict(set)
        
        # 构建邻接表表示图
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        def dfs(i: int, pre: int) -> bool:
            """
            深度优先搜索检查节点 i 是否能访问且不形成环
            
            :param i: 当前节点索引
            :param pre: 上一个访问的节点索引，用于跳过回边
            :return: 如果当前子树无环且所有节点均被访问，则返回 True；否则返回 False
            """
            visited[i] = 1
            for v in adj[i]:
                if v != pre and (visited[v] or not dfs(v, i)):
                    return False
            return True
        
        # 检查从根节点开始的搜索是否无环且所有节点被访问
        valid_dfs = dfs(0, -1)
        
        # 验证所有节点均被访问
        all_visited = sum(visited) == n

        return valid_dfs and all_visited



class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        visited, adj = [0] * n, collections.defaultdict(set)
        
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        def dfs(i: int, pre: int) -> bool:
            visited[i] = 1
            for v in adj[i]:
                if v != pre and (visited[v] or not dfs(v, i)):
                    return False
            return True
        
        valid_dfs = dfs(0, -1)
        all_visited = sum(visited) == n

        return valid_dfs and all_visited

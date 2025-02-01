
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # 使用路径压缩和按秩合并优化的并查集初始化
        def uf(c):
            if parent[ord(c) - ord('a')] != c:
                parent[ord(c) - ord('a')] = uf(parent[ord(c) - ord('a')])
            return parent[ord(c) - ord('a')]

        # 初始化并查集，每个字符初始为自己父节点
        parent = [c for c in string.ascii_lowercase]
        
        # 处理等号约束条件
        for eq in equations:
            if eq[1] == '=':
                # 合并等号两边的连通分量
                root_x = uf(eq[0])
                root_y = uf(eq[-1])
                parent[root_x] = root_y
        
        # 检查非等号约束条件
        for eq in equations:
            if eq[1] == '!':
                # 如果非等号两边属于同一个连通分量，返回False
                if uf(eq[0]) == uf(eq[-1]):
                    return False
        
        return True

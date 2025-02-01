
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 使用并查集（Union-Find）来处理连接关系
        class UF:
            def __init__(self, n):
                self.p = list(range(n))  # 初始化父节点数组

            def union(self, x, y):
                self.p[self.find(x)] = self.find(y)  # 将y的根节点作为x的根节点的父节点

            def find(self, x):
                if x != self.p[x]: 
                    self.p[x] = self.find(self.p[x])  # 路径压缩
                return self.p[x]

        uf, res, m = UF(len(s)), [], collections.defaultdict(list)
        
        # 将指定的字符对进行合并操作
        for x, y in pairs: 
            uf.union(x, y)

        # 按连通分量收集字符
        for i in range(len(s)): 
            m[uf.find(i)].append(s[i])

        # 对每个连通分量中的字符进行排序（逆序）
        for comp_id in m.keys(): 
            m[comp_id].sort(reverse=True)

        # 构建结果字符串
        for i in range(len(s)): 
            res.append(m[uf.find(i)].pop())

        return ''.join(res)

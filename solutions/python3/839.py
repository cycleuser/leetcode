
class Solution:
    def numSimilarGroups(self, A):
        """
        初始化结果计数器、图结构和访问集合。
        
        :param A: 字符串列表，表示需要判断相似组的数量的字符串集合
        """

        def explore(s):
            """
            深度优先搜索函数，用于标记当前节点及其所有可达且未被标记过的邻接节点为已访问。

            :param s: 当前正在探索的字符串
            """
            visited.add(s)
            for v in edges[s]:
                if v not in visited:
                    explore(v)

        res, edges, visited = 0, {}, set()

        # 如果 A 的长度大于或等于 A 中最长字符串的两倍，进行特定规则的相似性检查
        if len(A) >= 2 * len(A[0]):
            strs = set(A)
            for s in A:
                if s not in edges: edges[s] = set()
                for i in range(len(s) - 1):
                    for j in range(i + 1, len(s)):
                        new_s = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
                        if new_s in strs:
                            edges[s].add(new_s)
                            if new_s in edges: 
                                edges[new_s].add(s)
                            else: 
                                edges[new_s] = {s}
        # 否则，进行常规的相似性检查
        else:
            for s in A:
                if s not in edges: edges[s] = set()
                for t in A:
                    if s != t:
                        same = 0
                        for i, c in enumerate(t):
                            if c == s[i]: same += 1
                        if same == len(s) - 2: 
                            edges[s].add(t)
                            if t in edges: 
                                edges[t].add(s)
                            else: 
                                edges[t] = {s}
        
        # 对于未被访问过的字符串，进行深度优先搜索并增加结果计数器
        for s in A:
            if s not in visited:
                res += 1
                explore(s)

        return res

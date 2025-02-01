
class Solution(object):
    # 定义求解外星文排序的方法
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) == 1:
            return words[0]

        # 辅助函数进行深度优先搜索
        def dfs(i):
            """
            :param i: 当前节点索引
            :return: True 表示没有环，False 表示有环
            """
            visited[i] = 0
            for v in graph[i]:
                if visited[v] == 0 or (visited[v] == -1 and not dfs(v)):
                    return False
            order.append(chr(97 + i))
            visited[i] = 1
            return True

        # 初始化图和访问数组，以及结果列表
        graph, visited, order = collections.defaultdict(set), [1] * 26, []
        
        # 构建图结构
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    graph[ord(c1) - ord("a")].add(ord(c2) - ord("a"))
                    break
        
        # 将所有字符标记为未访问
        for c in (w1 + w2 for w1, w2 in zip(words, words[1:])):
            visited[ord(c) - ord("a")] = -1

        # 深度优先搜索构建拓扑排序
        for i in range(26):
            if visited[i] == -1 and not dfs(i): 
                return ""
        
        # 返回结果，注意反转顺序
        return "".join(order)[::-1]

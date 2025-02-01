
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # 使用深度优先搜索，从某个单词出发找到最长的单词链长度
        def dfs(w1, size):
            return max([dfs(w2, size + 1) for w2 in graph[w1]], default = size)
        
        from collections import defaultdict
        
        # 构建一个图结构，节点是按单词长度分组后的列表
        graph = defaultdict(list)
        for w in words:
            graph[len(w)].append(w)
        
        # 填充图结构：对于每个单词w1，在比其长的单词中查找可能的前驱
        for w1 in words:
            for w2 in graph[len(w1) + 1]:
                for i in range(len(w2)):
                    if w2[:i] + w2[i + 1:] == w1:
                        graph[w1].append(w2)
        
        # 计算每个单词的最长链长度，返回其中的最大值
        return max(dfs(w, 1) for w in words)

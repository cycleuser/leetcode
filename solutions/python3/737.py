
class Solution:
    def areSentencesSimilarTwo(self, words1: list[str], words2: list[str], pairs: list[tuple[str, str]]) -> bool:
        """
        判断两个句子是否相似。句子的相似性由单词对定义，如果两个单词在任何一个对中，则它们是相似的。
        
        :param words1: 第一个句子的单词列表
        :param words2: 第二个句子的单词列表
        :param pairs: 一系列单词对的集合
        :return: 如果两句话通过给定的规则可以互换则返回 True，否则返回 False
        """
        
        def dfs(node, Id):
            """深度优先搜索函数，用于标记节点所属连通分量"""
            cc[node] = Id
            for v in adj[node]:
                if v not in cc:
                    dfs(v, Id)
                    
        l1, l2, adj, cc = len(words1), len(words2), collections.defaultdict(set), {}
        
        # 如果两个句子长度不同，直接返回 False
        if l1 != l2:
            return False
        
        # 构建图的邻接表表示形式
        for a, b in pairs:
            adj[a].add(b)
            adj[b].add(a)
            
        # 使用 DFS 标记每个单词所在的连通分量
        for Id, k in enumerate(adj):
            if k not in cc:
                dfs(k, Id)
                
        # 检查两个句子的对应位置上的单词是否相似
        for w1, w2 in zip(words1, words2):
            if w1 not in cc or w2 not in cc:
                if w1 != w2:
                    return False
            elif cc[w1] != cc[w2]:
                return False
                
        return True

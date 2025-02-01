
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # 查找根节点的递归函数
        def root(s):
            # 如果当前字符串是其自身的父节点，说明它已经是根节点
            return s if parent[s] == s else root(parent[s])

        # 初始化并查集中的每个单词及其自身作为父节点
        parent = {s: s for s in [c for sy in synonyms for c in sy] + text.split()}

        # 合并同义词的根节点
        for a, b in synonyms:
            parent[root(a)] = root(b)

        # BFS初始化，初始为空字符串列表
        bfs = [""]
        
        # 对于每个单词，查找其根节点，并构建新的句子组合
        for t in text.split():
            r = root(t)
            bfs = [s + " " + w for s in bfs for w in parent if root(w) == r]

        # 返回所有可能的句子组合并排序
        return sorted(s[1:] for s in bfs)

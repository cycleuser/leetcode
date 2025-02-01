
class Solution:
    # 定义一个用于将字符串S中包含指定单词列表words中的单词添加粗体标签的方法
    
    def addBoldTag(self, S: str, words: list[str]) -> str:
        trie, n, mask, res = {}, len(S), set(), ""
        
        # 构建前缀树（Trie）
        for w in words:
            cur = trie
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["#"] = cur.get("#", set()) | {w}
        
        # 遍历字符串S并构建mask集合，记录需要加粗的部分的索引范围
        for i in range(n):
            cur, j = trie, i
            while j < n and S[j] in cur:
                cur = cur[S[j]]
                if "#" in cur:
                    mask |= {ind for ind in range(i, j + 1)}
                j += 1
        
        # 根据mask集合生成最终的加粗字符串res
        for i in range(n):
            if i in mask and (not i or i - 1 not in mask):
                res += "<b>"
            res += S[i]
            if i in mask and (i == n - 1 or i + 1 not in mask):
                res += "</b>"
        
        return res

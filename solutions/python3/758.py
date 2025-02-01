
class Solution:
    # 初始化解决方案类

    def boldWords(self, words, S):
        # 构建Trie树，存储单词列表，并标记以#结束的单词
        trie, n, mask, res = {}, len(S), set(), ""
        
        for w in words:
            cur = trie
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            # 使用集合进行标记，避免重复添加相同的单词
            cur["#"] = cur.get("#", set()) | {w}

        # 遍历字符串S，并构建mask集合，记录需要加粗的位置
        for i in range(n):
            cur, j = trie, i
            while j < n and S[j] in cur:
                cur = cur[S[j]]
                if "#" in cur:
                    mask |= {ind for ind in range(i, j + 1)}
                j += 1

        # 根据mask集合生成最终结果字符串，加粗指定位置的字符
        for i in range(n):
            if i in mask and (not i or i - 1 not in mask):
                res += "<b>"
            res += S[i]
            if i in mask and (i == n - 1 or i + 1 not in mask):
                res += "</b>"

        return res

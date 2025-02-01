
class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        """
        :param wordlist: 一个单词列表
        :param queries: 需要检查的查询单词列表
        :return: 对于每个查询单词，返回最接近的正确拼写形式或者空字符串（如果不存在）
        """

        # 使用集合存储所有单词以实现快速查找
        st = set(wordlist)
        # 用于存储大写字母单词及其小写对应词
        cap = {}
        # 用于存储去掉了元音字母后的单词及其原始单词
        vow = {}

        # 构建容错字典
        for w in wordlist:
            newC = w.lower()
            newW = "".join(c if c not in "aeiou" else "*" for c in newC)
            if newC not in cap:
                cap[newC] = w
            if newW not in vow:
                vow[newW] = w

        # 对每个查询进行处理
        for i, w in enumerate(queries):
            if w in st:
                pass  # 已存在于单词列表中，不做修改
            elif w.lower() in cap:
                queries[i] = cap[w.lower()]  # 大写形式匹配，使用正确的拼写
            else:
                new = "".join(c if c not in "aeiou" else "*" for c in w.lower())
                if new in vow:
                    queries[i] = vow[new]  # 替换元音后的形式匹配，使用正确的拼写
                else:
                    queries[i] = ""  # 未找到匹配项

        return queries

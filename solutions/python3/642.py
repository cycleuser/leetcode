
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        """
        初始化类对象，设置根节点和排名字典。
        :param sentences: 输入的句子列表
        :param times: 各句子出现次数
        """
        self.cur = self.root = {}
        self.rank = collections.defaultdict(int)
        for i, s in enumerate(sentences):
            self.s = s
            self.rank[s] = times[i]
            self.input('#')

    def move(self, c: str) -> None:
        """
        移动到当前节点的子节点。
        :param c: 当前字符
        """
        if c not in self.cur:
            self.cur[c] = {}
        self.cur = self.cur[c]
        if 'sentences' not in self.cur:
            self.cur['sentences'] = []

    def addSentence(self) -> None:
        """
        添加句子到当前节点。
        :return: 无
        """
        self.cur = self.root
        for c in self.s:
            self.move(c)
            self.search()
            heapq.heappush(self.cur['sentences'], [-self.rank[self.s], self.s])

    def search(self) -> List[str]:
        """
        搜索并返回排名最高的三个句子。
        :return: 三个句子列表
        """
        q, used, i = [], set(), 0
        while i < 3 and self.cur['sentences']:
            r, s = heapq.heappop(self.cur['sentences'])
            if s not in used:
                used.add(s)
                q.append([r, s])
                i += 1
        for r, s in q:
            heapq.heappush(self.cur['sentences'], [r, s])
        return [s for r, s in q]

    def input(self, c: str) -> List[str]:
        """
        处理输入字符，返回当前可能的建议列表。
        :param c: 输入字符
        :return: 三个句子列表或空列表
        """
        if c == '#':
            self.rank[self.s] += 1
            self.addSentence()
            self.s = ''
            self.cur = self.root
            return []
        else:
            self.s += c
            self.move(c)
            return self.search()


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

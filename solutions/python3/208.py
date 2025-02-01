
class Trie:

    def __init__(self):
        """
        初始化字典树数据结构。
        Initialize the Trie data structure.
        """
        self.root = {}

    def move(self, word, mod):
        """
        将单词插入到字典树中或检查是否存在前缀/单词。
        Insert a word into the trie or check for prefix existence.

        :param word: 要处理的字符串
        :type word: str
        :param mod: 操作模式，1-插入，2-查找单词，3-查找前缀
        :type mod: int
        :return: 根据操作模式返回相应的布尔值或None
        :rtype: bool or None
        """
        cur = self.root
        for c in word:
            if c not in cur:
                if mod != 1:
                    return False
                cur[c] = {}
            cur = cur[c]
        if mod == 1:
            cur['#'] = None  # 标记单词结束
        else:
            return mod == 3 or '#' in cur

    def insert(self, word: str) -> None:
        """
        将一个单词插入到字典树中。
        Insert a word into the trie.

        :param word: 要插入的单词
        :type word: str
        """
        return self.move(word, 1)
        
    def search(self, word: str) -> bool:
        """
        检查一个单词是否存在于字典树中。
        Returns if the word is in the trie.

        :param word: 要查找的单词
        :type word: str
        :return: 如果单词存在返回True，否则返回False
        :rtype: bool
        """
        return self.move(word, 2)

    def startsWith(self, prefix: str) -> bool:
        """
        检查字典树中是否存在以给定前缀开头的任何单词。
        Returns if there is any word in the trie that starts with the given prefix.

        :param prefix: 要查找的前缀
        :type prefix: str
        :return: 如果存在以该前缀开头的单词返回True，否则返回False
        :rtype: bool
        """
        return self.move(prefix, 3)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

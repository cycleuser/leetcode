

class TrieNode:
    # 构造器初始化节点，每个节点包含26个子节点指针和一个标记是否为单词结尾的标志
    def __init__(self):
        self.children = [None] * 26
        self.last = False


class WordDictionary:

    def __init__(self):
        # 初始化字典树根节点
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        # 添加单词到数据结构中
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            if not curr.children[ord(char) - ord("a")]:
                curr.children[ord(char) - ord("a")] = TrieNode()
            curr = curr.children[ord(char) - ord("a")]
        curr.last = True

    def search(self, word):
        # 搜索单词，允许通配符"."
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        words = [self.root]
        for char in word:
            if char == ".":
                # 通配符匹配所有可能的子节点
                words = [child for node in words for child in node.children if node and child]
            else:
                # 普通字符仅匹配对应的子节点
                words = [node.children[ord(char) - ord("a")] for node in words if node and node.children[ord(char) - ord("a")]]
        # 判断是否找到单词或其结尾标记为True的节点
        if words and (words[-1] is None or words[-1].last):
            return True
        else:
            return any([node.last for node in words if node and node.last])


# 你的WordDictionary对象将被实例化并调用如下：
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

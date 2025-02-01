
from collections import defaultdict

class MagicDictionary:

    def __init__(self):
        """
        初始化数据结构。
        """
        # 使用defaultdict来存储修改后的单词和其被替换的字符
        self.var = defaultdict(set)

    def buildDict(self, dict):
        """
        通过一个单词列表构建字典。
        :param dict: List[str] - 包含要添加到字典中的单词列表。
        :return: None
        """
        for w in dict:
            for i in range(len(w)):
                # 将每个字符替换为'_'，并记录该位置的被替换单词
                self.var[(i, w[:i] + '_' + w[i + 1:])].add(w[i])

    def search(self, word):
        """
        检查是否可以通过修改一个字符使得单词与字典中的任何一个单词匹配。
        :param word: str - 要查找的单词
        :return: bool - 是否存在这样的单词
        """
        for i in range(len(word)):
            # 替换当前字符，检查是否有其他字符可以替换它
            if self.var[(i, word[:i] + '_' + word[i + 1:])] - {word[i]}:
                return True
        return False


# 初始化MagicDictionary对象并调用相关方法
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)


class WordDistance:

    def __init__(self, words):
        """
        初始化字典和索引集合，用于存储单词及其位置。
        Initialize the dictionary and index set to store words and their positions.
        :param words: 初始词列表
        :type words: List[str]
        """
        self.d = {}
        self.ind = collections.defaultdict(set)
        for i, w in enumerate(words):
            self.ind[w].add(i)

    def shortest(self, word1, word2):
        """
        计算两个单词之间的最短距离。
        Calculate the shortest distance between two words.
        :param word1: 第一个单词
        :type word1: str
        :param word2: 第二个单词
        :type word2: str
        :return: 最短距离
        :rtype: int
        """
        if (word1, word2) not in self.d:
            # 计算并存储两个单词之间的最短距离
            # Calculate and store the shortest distance between two words
            self.d[(word1, word2)] = self.d[(word2, word1)] = min(abs(j - i)
                                                                  for i in self.ind[word1]
                                                                  for j in self.ind[word2])
        return self.d[(word1, word2)]

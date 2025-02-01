
from collections import defaultdict

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        """
        初始化字典，构建一个映射关系。使用哈希表存储单词的缩写形式和实际单词。
        :param dictionary: 初始词汇列表
        """
        self.pool = defaultdict(set)
        for w in dictionary:
            # 计算单词的缩写形式
            abbr = (w[0] + str(len(w) - 2) + w[-1]) if len(w) > 2 else w
            # 将实际单词添加到对应的缩写集合中
            self.pool[abbr].add(w)

    def isUnique(self, w: str) -> bool:
        """
        判断给定的单词是否唯一。如果该单词在哈希表中的映射集合不包含这个单词，则返回True。
        :param w: 待检查的单词
        :return: 如果单词是唯一的则返回True，否则返回False
        """
        return not self.pool[(w[0] + str(len(w) - 2) + w[-1]) if len(w) > 2 else w] - {w}

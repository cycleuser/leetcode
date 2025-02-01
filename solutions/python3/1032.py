
import functools
from collections import defaultdict

class StreamChecker(object):

    # 初始化Trie树，用于存储单词
    def __init__(self, words):
        # 使用lambda函数定义一个字典工厂函数
        T = lambda: defaultdict(T)
        # 创建Trie树根节点
        self.trie = T()
        # 构建Trie树并插入所有单词
        for w in words:
            functools.reduce(dict.__getitem__, w, self.trie)['#'] = True
        # 初始化等待列表，用于存储当前正在匹配的路径节点
        self.waiting = []

    # 查询函数，判断当前字母是否构成某个单词
    def query(self, letter):
        # 更新等待列表：移除不符合条件的节点，并加入新字母对应的新节点
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        # 检查当前等待列表是否包含结束符'#'
        return any("#" in node for node in self.waiting)

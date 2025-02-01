
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list) -> list:
        """
        寻找最短转换序列，将 beginWord 变换为 endWord，并且每次只能改变一个字母。
        
        :param beginWord: 初始单词
        :param endWord: 目标单词
        :param wordList: 可用的单词列表
        :return: 从 beginWord 到 endWord 的最短转换序列，如果没有找到，则返回空列表
        """
        words, res, layer = set(wordList), [], {beginWord: [[beginWord]]}
        
        # 当当前层不为空时继续执行
        while layer:
            newlayer = collections.defaultdict(list)
            
            for w in layer:
                # 如果找到目标单词，将路径添加到结果中
                if w == endWord:
                    res.extend(layer[w])
                else:
                    # 构造新的候选单词，并更新下一层
                    for i in range(len(w)):
                        for c in string.ascii_lowercase:
                            neww = w[:i] + c + w[i + 1:]
                            if neww in words:
                                newlayer[neww].extend([j + [neww] for j in layer[w]])
            # 更新可使用的单词集
            words -= set(newlayer.keys())
            # 进入下一层
            layer = newlayer
        
        return res

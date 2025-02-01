
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        """
        Chinese:
        题目要求从一个起始单词通过一系列变换到达目标单词，每次变换只能改变一个字母，并且中间结果必须在给定的字典中。
        本题使用了广度优先搜索（BFS）的方法来寻找最短路径。

        English:
        The problem requires transforming a start word into an end word by changing one letter at a time, with each intermediate result being in the given dictionary.
        This solution uses Breadth-First Search (BFS) to find the shortest path.
        """

        words, layer = set(wordList), {beginWord: [[beginWord]]}
        """
        Chinese:
        初始化一个字典`layer`，其键为当前单词，值为其到达路径。同时将所有词汇加入集合`words`中。
        
        English:
        Initialize a dictionary `layer`, with keys as the current words and values as their paths. Also, add all words to the set `words`.
        """

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    return len(layer[w][0])
                else:
                    for i in range(len(w)):
                        for c in string.ascii_lowercase:
                            neww = w[:i] + c + w[i + 1:]
                            if neww in words:
                                newlayer[neww] += [j + [neww] for j in layer[w]]
            """
            Chinese:
            对于当前层中的每个单词，尝试每一种可能的单个字母替换。如果新生成的单词在词典中，则将其添加到新的层中。
            
            English:
            For each word in the current layer, try every possible single-letter substitution. If the new word is in the dictionary, add it to the new layer.
            """

            words -= set(newlayer.keys())
            layer = newlayer
        """
        Chinese:
        移除已经访问过的单词，更新当前层为新的层。

        English:
        Remove visited words and update the current layer to the new one.
        """

        return 0

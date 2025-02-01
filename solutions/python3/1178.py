
from itertools import combinations as cb

class Solution:
    """
    该类用于解决寻找有效单词数量的问题。
    """

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        计算给定谜题中有效单词的数量。

        参数:
        words (List[str]): 一个包含单词的列表。
        puzzles (List[str]): 一个包含谜题字符串的列表，每个谜题字符串由多个字符组成。

        返回:
        List[int]: 每个谜题的有效单词数量列表。
        """
        from collections import Counter

        # 统计每个单词经过排序和去重后的频率
        cnt = Counter(''.join(sorted(set(w))) for w in words)

        # 计算每个谜题中的有效单词数量
        return [
            sum(
                cnt[''.join(sorted(s + (p[0], )))]
                for l in range(len(p))
                for s in cb(p[1:], l)
            )
            for p in puzzles
        ]

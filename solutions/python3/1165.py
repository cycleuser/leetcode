
class Solution:
    # 计算在键盘k上按下单词word中的每个字符所需的总时间

    def calculateTime(self, k: str, word: str) -> int:
        # 使用zip将k的首字符与word的每个字符配对，计算相邻字符在键盘上的距离之和
        return sum(abs(k.index(a) - k.index(b)) for a, b in zip(k[0] + word, word))

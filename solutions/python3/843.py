
import collections
import itertools

class Solution:
    # 寻找秘密单词的解决方案类
    def findSecretWord(self, wordlist, master):
        # 尝试次数初始化为0
        n = 0
        while n < 6:
            # 统计两个词完全不匹配的次数
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if sum(i == j for i, j in zip(w1, w2)) == 0)
            # 选择当前猜测单词，使其在统计中出现次数最少（即与其它单词不匹配的可能性最小）
            guess = min(wordlist, key=lambda w: count[w])
            # 使用Master接口进行猜测
            n = master.guess(guess)
            # 更新wordlist为与猜测单词n个位置匹配的单词列表
            wordlist = [w for w in wordlist if sum(i == j for i, j in zip(w, guess)) == n]

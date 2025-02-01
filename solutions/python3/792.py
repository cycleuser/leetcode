
class Solution:
    # 检查字符串s是否是word的子序列
    def check_subsequence(self, s, word):
        index = 0
        # 遍历word中的每个字符
        for char in word:
            # 在s中查找char，从当前index开始
            index = s.find(char, index) + 1
            # 如果找不到，则不是子序列
            if not index: 
                return False
        # 所有字符都匹配上了
        return True

    # 计算words中有多少字符串是S的子序列
    def numMatchingSubseq(self, S, words):
        # 对每个word，调用check_subsequence检查是否是子序列
        return sum((self.check_subsequence(S, word) for word in words))

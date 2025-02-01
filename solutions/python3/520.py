
class Solution:
    # 检查给定单词的使用大写字母方式是否正确

    def detectCapitalUse(self, word: str) -> bool:
        # 如果首字母大写且后续全部小写，或全为大写，或全为小写，则符合要求
        return word[0].isupper() and word[1:].islower() or word.isupper() or word.islower()


class Solution:
    # 反转字符串中的单词
    def reverseWords(self, s: str) -> str:
        # 使用split()将字符串按空格分割成单词列表，[::-1]反转列表顺序
        # 最后使用" ".join()将单词列表重新组合成一个字符串，并用空格分隔
        return " ".join(s.split()[::-1])

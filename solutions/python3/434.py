
class Solution:
    # 计算字符串s中的单词个数
    def countSegments(self, s):
        """
        :param s: 字符串（str）
        :return: 返回字符串中单词的数量 (int)
        """
        return len(s.split())

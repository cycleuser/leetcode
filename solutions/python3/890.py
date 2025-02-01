
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        # 初始化结果列表
        res = []

        for w in words:
            # 用于映射字符的字典，分别从word到pattern和pattern到word进行双向映射
            mp12, mp21, match = {}, {}, True

            # 遍历单词w和模式字符串pattern中的字符对
            for c1, c2 in zip(w, pattern):
                # 检查当前字符是否已经存在于字典中，且对应关系不匹配，则标记为非匹配
                if (c1 in mp12 and mp12[c1] != c2) or (c2 in mp21 and mp21[c2] != c1):
                    match = False
                    break

                # 将当前字符映射加入字典中
                mp12[c1], mp21[c2] = c2, c1

            # 如果当前单词符合模式，则添加至结果列表
            if match:
                res.append(w)

        return res

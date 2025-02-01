    class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # 创建一个字典，用于快速查找字符在新排序规则中的位置
        ind = {c: i for i, c in enumerate(order)}
        
        # 遍历相邻的单词对
        for a, b in zip(words, words[1:]):
            # 检查较短单词是否为较长单词的前缀，如果是，则顺序错误
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            
            # 遍历两个单词对应的字符
            for s1, s2 in zip(a, b):
                # 如果当前字符在新排序规则中的位置小于另一个，说明已找到正确顺序，跳出循环
                if ind[s1] < ind[s2]:
                    break
                # 若相等，则继续检查下一个字符
                elif ind[s1] == ind[s2]:
                    continue
                # 否则，顺序错误
                else:
                    return False
        
        # 如果所有单词都符合新排序规则，则返回 True
        return True
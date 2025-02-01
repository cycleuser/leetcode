
class Solution:
    # 定义一个方法用于检查单词是否可以由字典中的其他单词拼接而成
    def findAllConcatenatedWordsInADict(self, words):
        # 辅助函数，递归检查子字符串是否存在字典中
        def check(w, st):
            if w in st:  # 如果当前单词存在于集合中，则直接返回True
                return True
            for i in range(1, len(w)):  # 遍历所有可能的分割点
                if w[:i] in st and check(w[i:], st):  # 检查前缀和后缀是否都在字典中
                    return True
            return False

        # 将输入单词转换为集合，方便查找
        w_set, res = set(words), []
        
        for w in words:
            w_set.remove(w)  # 从集合中移除当前检查的单词
            
            if check(w, w_set):  # 如果当前单词可以通过字典中的其他单词拼接而成，则加入结果列表
                res += w,
            
            w_set.add(w)  # 将当前单词重新添加回集合，为下次循环做准备

        return res  # 返回所有可以由字典中单词拼接而成的单词

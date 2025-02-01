
class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        
        方法说明：使用集合加速前缀查找，遍历句子中的每个单词，寻找其最短前缀在词典中，并替换之。
        """
        
        # 使用集合存储词典以加快查找速度
        s = set(dict)
        
        # 将句子按空格分割成单词列表
        sentence = sentence.split()
        
        # 遍历每个单词
        for j, w in enumerate(sentence):
            # 检查该单词的每一个前缀是否在词典中
            for i in range(1, len(w)):
                if w[:i] in s:
                    # 如果找到，则替换为最短前缀
                    sentence[j] = w[:i]
                    break
        
        # 将处理后的单词列表重新组合成句子并返回
        return " ".join(sentence)

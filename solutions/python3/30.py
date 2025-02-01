
class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        """
        找出给定字符串中包含所有单词的子串起始位置。
        
        :param s: 输入字符串
        :param words: 单词列表
        :return: 包含所有单词的子串起始位置列表
        """
        if not s or not words:
            return []
        
        from collections import Counter
        
        # 统计每个单词出现次数
        cnt = Counter(words)
        
        # 计算所有单词总长度
        l_words = len(words[0]) * len(words)
        
        # 单词的单个长度
        l_word = len(words[0])
        
        # 单词数量
        cnt_words = len(words)
        
        res = []
        
        for i in range(len(s) - l_words + 1):
            cur, j = dict(cnt), i
            
            for _ in range(cnt_words):
                w = s[j:j + l_word]
                
                if w in cur:
                    # 如果单词计数为1，移除该键值对
                    if cur[w] == 1:
                        cur.pop(w)
                    else:
                        cur[w] -= 1
                    
                else:
                    break
                
                j += l_word
            
            if not cur: 
                res.append(i)
        
        return res

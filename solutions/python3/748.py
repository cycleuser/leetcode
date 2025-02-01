
class Solution:
    def shortestCompletingWord(self, lp, words):
        """
        :param lp: 字符串，待匹配的字符序列（英文）
        :param words: 列表，包含多个字符串，寻找最短完成词（英文）
        :return: 最短完成词（英文）
        """
        
        # 统计lp中的字母频率，并过滤非字母字符
        cntr_lp = {k: v for k, v in collections.Counter(lp.lower()).items() if k.isalpha()}
        
        # 初始化结果，存放最短的完成词及其长度
        res = [None, None]
        
        # 遍历words中的每个单词
        for word in words:
            # 统计当前word的小写形式的字母频率
            check = collections.Counter(word.lower())
            
            # 判断check是否包含cntr_lp中所有字符且数量足够，利用all和生成器表达式实现
            if all(True if k in check and v <= check[k] else False for k, v in cntr_lp.items()):
                # 更新结果：如果当前word比记录的短或首次找到有效词时更新
                if not any(res) or len(word) < res[1]:
                    res = [word, len(word)]
        
        return res[0]

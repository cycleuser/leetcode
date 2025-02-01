
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        判断给定的缩写abbr是否可以合法地表示单词word。
        
        参数：
            word (str): 原始单词，每个字符都是小写字母。
            abbr (str): 缩写形式，可能包含字母和数字。

        返回值：
            bool: 如果abbr是合法的word缩写，则返回True；否则返回False。
        """
        i = num = 0
        for c in abbr:
            if c.isdigit():
                # 数字字符处理：确保首字符不是'0'，且累加数字
                if num == 0 and c == '0':
                    return False
                num = num * 10 + int(c)
            else:
                # 非数字字符处理：跳过数字部分，检查实际单词的对应位置
                if num:
                    i += num
                    num = 0
                if i >= len(word) or word[i] != c:
                    return False
                i += 1
        # 最后判断是否完整匹配
        return i == len(word) if num == 0 else i + num == len(word)

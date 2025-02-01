
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        """
        :param pattern: 字符模式字符串
        :param str: 由空格分隔的单词组成的字符串
        :return: 如果str中的每个单词可以一一对应于pattern中的字符，则返回True，否则返回False
        """

        if len(str.split()) != len(pattern):
            return False

        dic = {}
        
        for word in str.split():
            # 检查当前模式字符是否已被映射过且不是当前单词
            if pattern[0] not in dic.values() and word not in dic:
                dic[word] = pattern[0]
            else:
                # 如果当前模式字符已经映射过或不匹配，则返回False
                if word not in dic or dic[word] != pattern[0]:
                    return False
            
            # 移除已处理的模式字符
            pattern = pattern[1:]
        
        return True

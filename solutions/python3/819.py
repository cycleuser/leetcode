
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        # 使用正则表达式提取所有单词，\w+ 表示一个或多个字母数字字符
        paragraph = re.findall(r"\w+", paragraph)
        
        # 初始化字典和最大频率记录
        dic = {}
        mx = [0, 0]
        
        # 遍历每个单词并处理
        for char in paragraph:
            char = char.lower()  # 转换为小写以忽略大小写差异
            
            if char not in banned:  # 如果该单词不在禁止列表中
                if char not in dic: 
                    dic[char] = 1  # 记录首次出现的频率
                else: 
                    dic[char] += 1  # 增加已存在的单词计数
                
                # 更新最大频率记录
                mx[0] = max(mx[0], dic[char])
                
                if mx[0] == dic[char]: 
                    mx[1] = char  # 当出现新最高频单词时更新结果

        return mx[1]  # 返回最频繁的非禁止单词


class Solution:
    # 定义一个类，用于解决第一个唯一字符的问题

    def firstUniqChar(self, s):
        """
        :param s: 输入字符串
        :return: 返回第一个唯一字符的索引，如果没有则返回-1
        """
        from collections import defaultdict  # 引入defaultdict方便统计字符出现次数
        
        dic = defaultdict(int)  # 使用defaultdict来存储每个字符及其出现次数
        
        for c in s:
            # 遍历字符串中的每一个字符，并更新其在字典中的计数
            dic[c] += 1
        
        for i, c in enumerate(s):
            # 第二次遍历，查找第一个唯一字符的索引
            if dic[c] == 1: 
                return i  # 如果找到唯一字符，返回其索引
        
        return -1  # 如果没有找到唯一字符，返回-1

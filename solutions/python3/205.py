
class Solution:
    # 类：解决方案

    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        :param s: 字符串s
        :param t: 字符串t
        :return: 如果字符串s和字符串t是同构的返回True，否则返回False
        """
        if len(s) != len(t):  # 判断两个字符串长度是否相等
            return False

        dic = {}  # 创建字典用于存储对应关系
        
        for i in range(len(s)):  # 遍历字符串s和t的每个字符
            if s[i] not in dic and t[i] not in dic.values():  # 如果当前字符在字典中没有映射且目标字符未被使用
                dic[s[i]] = t[i]  # 建立对应关系
            elif s[i] in dic and dic[s[i]] != t[i]:  # 如果已有映射但不匹配
                return False  # 返回False

        return True  # 完成遍历，返回True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        判断两个字符串是否互为异位词（即包含相同的字符且每个字符出现的次数相同）
        
        :param s: 第一个字符串
        :param t: 第二个字符串
        :return: 如果s和t是异位词返回True，否则返回False
        """
        # 直接比较排序后的字符串是否相等，简化了原始代码中计算ASCII码之和与集合比较的操作
        return sorted(s) == sorted(t)

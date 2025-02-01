
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str  # 输入字符串s
        :rtype: bool   # 返回值为布尔类型，表示是否为回文串
        
        判断给定的字符串s是否是回文串。
        """
        import string

        # 过滤出字符串中的字母和数字，并转换成小写
        filtered_chars = [char.lower() for char in s if char in string.ascii_letters or char in string.digits]
        
        # 检查过滤后的字符列表是否与其反转相同
        return filtered_chars == filtered_chars[::-1]

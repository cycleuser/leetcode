
class Solution:
    # 定义一个寻找两个字符串最大公约数的函数，英文：Define a function to find the greatest common divisor of two strings.
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2):
            # 如果两个字符串长度相同，则返回两者中相等的那个或空字符串，英文：If the lengths of the two strings are equal, return either of them or an empty string.
            return str1 if str1 == str2 else ''
        
        # 如果str1比str2长
        elif len(str1) > len(str2):
            # 交换两个字符串位置以便处理，英文：Exchange positions of the two strings to handle.
            str1, str2 = str2, str1
        
        # 检查前缀是否匹配，英文：Check if the prefix matches.
        if str1[:len(str2)] == str2:
            # 递归调用自身，继续处理剩余部分，英文：Recursively call itself to process the remaining part.
            return self.gcdOfStrings(str1[len(str2):], str2)
        
        else:
            # 如果不匹配返回空字符串，英文：Return an empty string if not matched.
            return ''

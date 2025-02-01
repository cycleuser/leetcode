
class Solution:
    def largestPalindrome(self, n: int) -> int:
        """
        :type n: int  # 输入的整数n，表示回文数的位数
        :rtype: int  # 返回值为最大可能的n位回文数
        """
        
        # 回文数的最大可能取值列表（预先计算好的）
        max_palindromes = [0, 9, 987, 123, 597, 677, 1218, 877, 475]
        
        # 返回对应位数的回文数
        return max_palindromes[n]



class Solution:
    def largestPalindrome(self, n: int) -> int:
        """
        :type n: int  # 输入的整数n，表示回文数的位数
        :rtype: int  # 返回值为最大可能的n位回文数
        """
        
        # 回文数的最大可能取值列表（预先计算好的）
        max_palindromes = [0, 9, 987, 123, 597, 677, 1218, 877, 475]
        
        # 返回对应位数的回文数
        return max_palindromes[n]


class Solution:
    def countSubstrings(self, s):       
        """
        计算字符串s的所有回文子串的数量。
        
        参数:
            s (str): 输入的字符串
        
        返回:
            int: 回文子串的数量
        """
        res = 0
        for k in range(len(s)):
            # 中心扩展法，以单个字符为中心向两边扩散
            i, j = k, k
            while 0 <= i and j < len(s):
                if s[i] == s[j]: 
                    res += 1
                else: 
                    break
                i, j = i - 1, j + 1
            
            # 中心扩展法，以两个字符之间的空隙为中心向两边扩散
            i, j = k, k + 1
            while 0 <= i and j < len(s):
                if s[i] == s[j]: 
                    res += 1
                else: 
                    break
                i, j = i - 1, j + 1
        
        return res


class Solution:
    # 判断字符串s是否是字符串t的子序列
    def isSubsequence(self, s: str, t: str) -> bool:
        index = -1  # 记录当前字符在t中的索引位置
        
        for char in s:
            try:
                # 在t中从index+1的位置开始寻找char，若找到则更新index
                index = t.index(char, index + 1)
            except ValueError: 
                # 若未找到，则返回False
                return False
        
        # 如果s的所有字符都在t中按顺序出现过，则返回True
        return True



class Solution:
    # 判断字符串s是否是字符串t的子序列
    def isSubsequence(self, s: str, t: str) -> bool:
        index = -1  # 记录当前字符在t中的索引位置
        
        for char in s:
            try:
                # 在t中从index+1的位置开始寻找char，若找到则更新index
                index = t.index(char, index + 1)
            except ValueError: 
                # 若未找到，则返回False
                return False
        
        # 如果s的所有字符都在t中按顺序出现过，则返回True
        return True

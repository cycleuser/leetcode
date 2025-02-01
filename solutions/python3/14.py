
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        寻找字符串列表中的最长公共前缀。
        
        :param strs: 字符串列表
        :type strs: List[str]
        :return: 最长公共前缀
        :rtype: str
        """
        j = 0
        
        # 当列表不为空且所有字符串长度大于j并且当前字符相同时，增加j的值
        while strs and all(len(strs[i]) > j and strs[i][j] == strs[i - 1][j] for i in range(1, len(strs))):
            j += 1
        
        # 返回前缀，如果j为0则返回空字符串
        return strs[0][:j] if j else ''


class Solution:
    def distinctSubseqII(self, S: str) -> int:
        """
        计算字符串S中所有不同子序列的个数，结果对10^9 + 7取模。
        
        Args:
            S (str): 输入字符串
        
        Returns:
            int: 不同子序列的个数
        """
        res, end = 0, collections.Counter()  # 初始化结果和记录每个字符最后出现位置的计数器
        for c in S:
            # 更新结果：当前字符的新子序列数量等于之前的结果翻倍加一减去该字符上次出现时的结果
            res, end[c] = (res * 2 + 1 - end[c]) % (10**9 + 7), res + 1  # 取模操作确保结果在int范围内
        return res % (10**9 + 7)  # 返回最终结果取模后的值

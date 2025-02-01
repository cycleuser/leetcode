
class Solution:
    # Python 代码优化和注释
    
    def frequencySort(self, s: str) -> str:
        """
        中文注释：使用计数器统计字符串中每个字符的频率，并按降序排序。
        英文注释：Use a counter to count the frequency of each character in the string and sort it in descending order.
        
        :param s: 输入的字符串
        :return: 按照字符出现次数从多到少重新排列后的字符串
        """
        from collections import Counter
        
        # 中文注释：使用collections.Counter统计字符频率
        # 英文注释：Use collections.Counter to count the frequency of characters.
        cnt = Counter(s)
        
        res = ''
        # 中文注释：遍历排序后的频率项，并构建结果字符串
        # 英文注释：Iterate over the sorted frequency items and build the result string.
        for k, v in sorted(cnt.items(), key=lambda x: -cnt[x[0]]):
            res += k * v
        
        return res

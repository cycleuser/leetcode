
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # 中文注释：获取所有出现次数小于k的字符的位置索引，包括首尾位置
        br = [-1] + [i for i, c in enumerate(s) if s.count(c) < k] + [len(s)]
        
        # 中文注释：如果分割后的子串只有一个，则返回原字符串长度；否则递归计算每个子串的最大满足条件的长度并取最大值
        return len(s) if len(br) == 2 else max(self.longestSubstring(s[br[i - 1] + 1:br[i]], k) for i in range(1, len(br)))

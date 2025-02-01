
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        # 初始化结果列表和计数器
        out = list()
        from collections import Counter
        
        # 初始窗口为 s[:len(p)-1] 和 p 的字符计数
        s_counter, p_counter = Counter(s[:len(p) - 1]), Counter(p)
        
        # 滑动窗口遍历字符串 s
        for i in range(len(p) - 1, len(s)):
            # 更新当前字符的计数值，并检查是否与目标计数器匹配
            s_counter[s[i]] += 1
            if s_counter == p_counter:
                out.append(i - len(p) + 1)
            
            # 移除窗口最左边的字符，保持窗口大小不变
            s_counter[s[i - len(p) + 1]] -= 1
            if s_counter[s[i - len(p) + 1]] == 0:
                del s_counter[s[i - len(p) + 1]]
        
        return out

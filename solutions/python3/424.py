
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # 初始化字典、起始位置和结束位置
        dic, start, end = {}, 0, 0
        
        # 遍历字符串，从1到len(s)
        for end in range(1, len(s) + 1):
            if s[end-1] not in dic:
                dic[s[end-1]] = 1
            else:
                dic[s[end-1]] += 1
            
            # 如果当前窗口中最多字符出现次数小于k，则继续扩大窗口
            if end - start - max(dic.values()) > k: 
                # 否则，减少起始位置字符的计数，并移动起始位置指针
                dic[s[start]] -= 1
                start += 1
        
        # 返回最终结果：结束位置减去起始位置即为最大长度
        return end - start

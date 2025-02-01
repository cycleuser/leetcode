
class Solution:
    # 定义一个类来解决最长不含重复字符的子字符串问题

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # 初始化起始位置和不同字符计数器
        start = distinct = 0
        # 使用字典记录每个字符出现次数
        cnt = collections.defaultdict(int)
        
        for c in s:
            # 更新当前字符的计数
            cnt[c] += 1
            # 如果当前字符是首次出现，则不同字符计数加一
            if cnt[c] == 1:
                distinct += 1
            
            # 当不同字符计数超过2时，调整起始位置和计数器
            if distinct > 2:
                cnt[s[start]] -= 1
                if not cnt[s[start]]:
                    distinct -= 1
                start += 1
        
        # 返回最长不含重复字符子字符串的长度
        return len(s) - start

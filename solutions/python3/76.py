
class Solution:
    # 定义一个类，用于解决最小窗口子串问题

    def minWindow(self, s: str, t: str) -> str:
        # 初始化字符计数器、目标字符串的集合、s的长度以及left标志变量
        cnt_s, cnt_t, n, left, r = {}, {}, len(s), set(t), -1
        
        # 计算t中每个字符出现次数
        for c in t:
            cnt_t[c] = cnt_t.get(c, 0) + 1

        L = l = 0
        while left < 0:  # 循环直到找到目标子串的左边界
            r += 1
            if r >= n:  # 超出s长度时结束循环
                return ""
            cnt_s[s[r]] = cnt_s.get(s[r], 0) + 1
            if s[r] in cnt_t and cnt_s[s[r]] == cnt_t[s[r]]:
                left += 1  # 当字符匹配且数量满足要求时，更新left

        R = r
        cnt_s[s[r]] -= 1
        
        # 寻找最小覆盖子串的右边界
        while l < r < n:
            cnt_s[s[r]] = cnt_s.get(s[r], 0) + 1
            while s[l] not in cnt_t or cnt_s[s[l]] > cnt_t[s[l]]:
                cnt_s[s[l]] -= 1
                l += 1
            if r - l < R - L:
                L, R = l, r  # 更新最小覆盖子串的边界

            r += 1
        
        return s[L:R + 1]  # 返回结果

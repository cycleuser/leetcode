
class Solution:
    def countLetters(self, S: str) -> int:
        """
        计算字符串S中，满足条件的连续子串数量。
        
        :param S: 输入的字符串
        :return: 满足条件的连续子串的数量
        
        例如：输入 "aaaba"，输出为 8。解释："aaa", "aa", "a", "a", "ba", "b"
        """
        from collections import Counter

        cnt = Counter()  # 使用Counter来统计字符出现次数
        i = res = 0      # 初始化索引i和结果res
        
        for j, c in enumerate(S):  # 遍历字符串S的每个字符及其索引
            cnt[c] += 1             # 更新当前字符计数
            
            while len(cnt) > 1:     # 当出现多个不同的字符时，调整起始位置i
                cnt[S[i]] -= 1       # 减少起始索引处字符的计数
                if not cnt[S[i]]:    # 如果该字符计数为0，则移除它
                    cnt.pop(S[i])
                i += 1               # 起始位置i右移

            res += j - i + 1         # 累加满足条件的子串数量
        
        return res

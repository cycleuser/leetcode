
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        获取最长不含重复字符的子字符串长度，最多包含k个不同字符。
        
        :param s: 输入字符串
        :param k: 最多允许的不同字符数
        :return: 符合条件的最大子串长度
        """
        if not k:  # 如果k为0，直接返回0
            return 0

        cnt = collections.Counter()  # 使用Counter统计滑动窗口内的字符数量
        i = res = 0  # 初始化左指针i和结果res

        for j, c in enumerate(s):  # 遍历字符串s的每个字符c，其索引为j
            while len(cnt) == k and c not in cnt:  # 当当前窗口内的不同字符数达到k且新加入的字符不在窗口内时
                cnt[s[i]] -= 1  # 减少左指针指向字符的计数值
                if cnt[s[i]] == 0:
                    cnt.pop(s[i])  # 如果该字符数量为0，从Counter中移除
                i += 1  # 移动左指针i

            cnt[c] += 1  # 增加当前字符c的计数值
            res = max(res, j - i + 1)  # 更新最大长度

        return res  # 返回结果res

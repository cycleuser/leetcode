
class Solution:
    # 定义一个类用于处理字符串

    def reverseWords(self, s):
        # 反转整个字符串
        l, r, n = 0, len(s) - 1, len(s)
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        # 分别反转每个单词
        l = r = 0
        while r < n:
            while r + 1 < n and s[r + 1] != " ":  # 找到空格，表示一个单词的结束
                r += 1
            i = r + 2  # 指向下一个单词的起始位置
            while l <= r:  # 反转当前单词
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            l = r = i  # 更新指针，准备处理下一个单词

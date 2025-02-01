
class Solution:
    # 定义一个辅助函数 find，用于判断字符串 s 是否是字符串 t 的子序列
    def findLUSlength(self, strs):
        def find(s, t):
            i = 0
            for c in t:
                if c == s[i]:
                    i += 1
                if i == len(s):
                    return True
            return False
        
        # 对字符串列表按长度降序排序，以便优先检查较长的字符串
        for s in sorted(strs, key=len, reverse=True):
            # 检查当前字符串 s 是否是其他任何字符串的子序列
            if sum(find(s, t) for t in strs) == 1:
                return len(s)
        
        # 如果没有找到满足条件的字符串，返回 -1
        return -1


class Solution:
    # 定义一个解决类，用于寻找平衡字符串的最小子串长度

    def balancedString(self, s: str) -> int:
        # cnt: 记录每个字符需要调整的数量，初始值为最大可能值
        # i: 左边界指针
        # res: 结果，初始化为输入字符串长度
        cnt, i, res = {c: max(s.count(c) - len(s) // 4, 0) for c in 'QWER'}, 0, len(s)
        
        # 遍历整个字符串s
        for j, c in enumerate(s):
            # 减少当前字符需要调整的数量
            cnt[c] -= 1
            
            # 如果左边界指针i满足条件，则尝试收缩窗口
            while i < len(s) and cnt[s[i]] < 0:
                cnt[s[i]] += 1
                i += 1
                
            # 检查当前窗口是否满足所有字符数量要求
            if not any(cnt[c] > 0 for c in 'QWER'):
                # 更新结果为当前最小的子串长度
                res = min(res, j - i + 1)
        
        return res

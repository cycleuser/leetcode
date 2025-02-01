
from collections import Counter

class Solution:
    def reorganizeString(self, S):
        """
        使用Counter统计字符出现次数，重新组织字符串。
        :param S: str, 输入的原始字符串
        :return: str, 重新组织后的字符串或空串（无法重组时）
        """
        
        cnt, res = Counter(S), ""
        while len(res) < len(S):
            # 获取当前剩余字符中出现次数最多的字符及其频次
            c, i = cnt.most_common()[0], 0
            
            # 如果连续相同字符超过1个或该字符计数为0，则寻找下一个最常见字符
            while i + 1 < len(cnt) and (res and res[-1] == c[0] or cnt[c[0]] == 0):
                c, i = cnt.most_common()[i + 1], i + 1
            
            # 如果找到的字符无法再用或其前一个也是相同字符，返回空串
            if not cnt[c[0]] or res and res[-1] == c[0]:
                return ""
            
            else: 
                # 将选中的字符添加到结果字符串中，并减少该字符计数
                res, cnt[c[0]] = res + c[0], cnt[c[0]] - 1
        
        return res

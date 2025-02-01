
class Solution:
    def longestDecomposition(self, S: str) -> int:
        # 初始化结果、左子串和右子串为空字符串
        res, l, r = 0, "", ""
        
        # 双指针遍历，一个从前往后，一个从后往前
        for i, j in zip(S, reversed(S)):
            # 动态构建左右子串
            l += i
            r = j + r
            
            # 如果左右子串相等，则找到了一个回文分割点
            if l == r:
                res += 1
                # 清空左右子串，准备下次比较
                l, r = "", ""
        
        return res

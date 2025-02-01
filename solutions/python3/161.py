
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """
        判断两个字符串是否仅通过一次编辑操作就能变为相同。
        
        英文注释：Determine if two strings can become the same after performing at most one edit operation.
        """
        l1, l2 = len(s), len(t)
        cnt, i, j = 0, 0, 0

        # 遍历两个字符串
        while i < l1 and j < l2:
            if s[i] != t[j]:
                cnt += 1
                # 根据长度调整索引
                if l1 < l2:
                    j -= 1
                elif l1 > l2:
                    i -= 1
            i += 1
            j += 1

        # 计算长度差值
        l = abs(l1 - l2)

        # 返回是否满足编辑距离条件
        return (cnt == 1 and l <= 1) or (cnt == 0 and l == 1)

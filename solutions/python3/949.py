
import itertools

# 中文注释：定义一个类，用于寻找给定数字组成的最大时间
class Solution:
    # 英文注释: Define a class to find the largest time from given digits
    def largestTimeFromDigits(self, A):
        h = m = -float("inf")  # 初始化最大小时和分钟为负无穷
        
        # 中文注释：遍历所有可能的排列组合
        # 英文注释: Traverse all possible permutations of the input list A
        for n1, n2, n3, n4 in itertools.permutations(A):
            hh, mm = n1 * 10 + n2, n3 * 10 + n4  # 组合成小时和分钟

            # 中文注释：检查组合是否合法，更新最大时间
            # 英文注释: Check if the combination is valid and update the maximum time
            if 0 <= hh <= 23 and 0 <= mm <= 59 and (hh > h or hh == h and mm > m):
                h, m = hh, mm

        sh = str(h) if h > 9 else "0" + str(h)  # 处理小时格式
        sm = str(m) if m > 9 else "0" + str(m)  # 处理分钟格式
        
        # 中文注释：返回合法的最大时间，否则返回空字符串
        # 英文注释: Return the valid maximum time or an empty string if none is found
        return sh + ":" + sm if 0 <= h <= 23 and 0 <= m <= 59 else ""

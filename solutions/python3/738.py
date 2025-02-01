
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        """
        :type N: int  # 输入整数N
        :rtype: int    # 返回一个整数
        
        解题思路：从右向左遍历数字的每一位，一旦发现某位比前一位小，则将该位置及其右边的所有位减一，
                  直到找到第一个不满足单调递增的位置，然后将其左边所有位保持不变（减1操作），右边全部变为9。
        """
        n, pos = str(N), 0
        for i, char in enumerate(n):
            # 如果当前位比前一位小，则需要调整数字使其单调递增
            if i > 0 and int(char) < int(n[i-1]):
                return int("".join(n[:pos]) + str(int(n[pos])-1) + "9" * (len(n)-1-pos)) \
                    if int(n[pos]) > 1 else int("9" * (len(n)-1-pos))
            # 记录第一个不满足单调递增的位置
            elif i > 0 and char != n[i-1]:
                pos = i
        return N

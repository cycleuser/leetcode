
class Solution:
    # 判断一个数是否是3的幂次方
    def isPowerOfThree(self, n: int) -> bool:
        i = 1
        # 使用循环计算3的幂次，直到i >= n
        while i < n:
            i *= 3
        # 检查最终结果是否等于n
        return i == n

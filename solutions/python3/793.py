
class Solution:

    # 计算给定数在阶乘中因子5的数量
    def count(self, num: int) -> int:
        cnt = 0
        while num:
            cnt += num // 5
            num //= 5
        return cnt
    
    # 查找预定义大小的最小整数，使其阶乘因子5的数量等于给定值K
    def preimageSizeFZF(self, K: int) -> int:
        l, r = 0, 2 ** 63 - 1
        while l < r:
            mid = (l + r) // 2
            if self.count(mid) < K:
                l = mid + 1
            else:
                r = mid
        return 5 - (l % 5) if self.count(l) == K else 0


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        # 计算最大公约数 (Greatest Common Divisor)
        def gcd(a, b):
            return a if not b else gcd(b, a % b)

        # 计算a和b的最小公倍数
        ab = a * b // gcd(a, b)
        # 计算a和c的最小公倍数
        ac = a * c // gcd(a, c)
        # 计算b和c的最小公倍数
        bc = b * c // gcd(b, c)
        # 计算ab、ac、bc的最小公倍数
        abc = ab * c // gcd(ab, c)

        # 二分查找l到r范围内的第n个丑数
        l, r = 1, 2 * 10 ** 9
        while l < r:
            mid = (l + r) // 2
            # 计算mid包含a、b、c的倍数的数量，减去ab、ac、bc的倍数数量，加上abc的倍数数量
            if mid // a + mid // b + mid // c - mid // ab - mid // ac - mid // bc + mid // abc < n:
                l = mid + 1  # 调整左边界
            else:
                r = mid       # 调整右边界
        return l

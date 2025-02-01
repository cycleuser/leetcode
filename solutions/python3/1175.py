
class Solution:
    # 定义一个类来解决排列问题

    def numPrimeArrangements(self, n: int) -> int:
        # primes 是一个包含所有小于100的质数列表
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        
        # 使用二分查找确定不大于 n 的质数数量
        cnt = bisect.bisect(primes, n)
        
        # 计算质数和非质数的排列组合数，并取模 (10 ** 9 + 7)
        return math.factorial(cnt) * math.factorial(n - cnt) % (10 ** 9 + 7)

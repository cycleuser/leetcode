
class Solution:

    def gcd(self, a: int, b: int) -> int:
        """
        计算两个数的最大公约数
        Calculate the greatest common divisor of two numbers.
        """
        while b:
            a, b = b, a % b
        return a

    def count(self, num: int, A: int, B: int, C: int) -> int:
        """
        计算num中包含A和B的倍数的数量，减去C的倍数的数量。
        Calculate the number of multiples of A and B up to num, subtracting the multiples of C.
        """
        return num // A + num // B - num // C

    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        """
        寻找第N个既是A的倍数又是B的倍数的数。
        Find the Nth positive number that is a multiple of both A and B.
        """
        l, r, C = 2, 2 ** 63 - 1, A * B // self.gcd(A, B)
        
        while l < r:
            mid = (l + r) // 2
            if self.count(mid, A, B, C) < N:
                l = mid + 1
            else:
                r = mid
        
        return l % (10 ** 9 + 7)

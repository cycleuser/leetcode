
class Solution:
    # 判断一个数是否为质数
    def isPrime(self, x: int) -> bool:
        if x < 2 or x % 2 == 0: 
            return x == 2
        for i in range(3, int(x**0.5) + 1, 2):
            if x % i == 0: 
                return False
        return True

    # 寻找从N开始的最小回文质数
    def primePalindrome(self, N: int) -> int:
        if 8 <= N <= 11: 
            return 11
        for x in range(10 ** (len(str(N)) // 2), 10**5):
            y = int(str(x) + str(x)[-2::-1])
            if y >= N and self.isPrime(y): 
                return y

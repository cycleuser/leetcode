
class Solution:
    # 计算斐波那契数列的第N项，使用递归方式实现
    def fib(self, N: int) -> int:
        # 如果N大于1，则返回fib(N-1)和fib(N-2)之和；否则直接返回N
        return self.fib(N - 1) + self.fib(N - 2) if N > 1 else N

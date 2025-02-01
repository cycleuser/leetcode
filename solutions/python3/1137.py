
class Solution:
    # 计算第n个tribonacci数，采用迭代方式优化空间复杂度
    def tribonacci(self, n: int) -> int:
        # 初始化前三个tribonacci数为0, 1, 1
        t0, t1, t2 = 0, 1, 1
        
        # 迭代计算第n个tribonacci数
        for _ in range(n):
            # 更新t0, t1, t2的值，准备进行下一次迭代
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        
        # 返回第n个tribonacci数
        return t0

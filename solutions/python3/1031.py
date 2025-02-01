
class Solution:
    # Python 解决方案类
    
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        
        # 前缀和数组 l 和 r，用于记录最大子段和
        l = [0] * n
        r = [0] * n
        
        # 计算前缀和 l 的初始值
        sm = 0 
        for i in range(L - 1):
            sm += A[i]
        for j in range(n - L + 1):
            sm += A[j + L - 1]
            for i in range(j + 1):
                r[i] = max(r[i], sm)
            sm -= A[j]
        
        # 计算前缀和 r 的初始值
        sm = 0
        for i in range(n - 1, n - L, -1):
            sm += A[i]
        for i in range(n - 1, L - 2, -1):
            sm += A[i - L + 1]
            for j in range(i + 1, n):
                l[j] = max(l[j], sm)
            sm -= A[i]
        
        # 计算最大和
        sm = 0
        res = 0
        
        # 遍历数组 A，计算两个不重叠子段的最大和
        for i in range(L - 1):
            sm += A[i]
        for j in range(n - L + 1):
            sm += A[j + L - 1]
            if j >= M:
                res = max(res, sm + l[j - 1])
            if j + L < n:
                res = max(res, sm + r[j + L])
            sm -= A[j]
        
        return res

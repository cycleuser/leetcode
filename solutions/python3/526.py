
# 中文注释：定义一个类来解决排列问题，其中countArrangement方法用于计算满足条件的排列个数。
class Solution:
    # 英文注释: Define a class to solve the arrangement problem. The countArrangement method is used to calculate the number of valid arrangements.
    
    memo = {}
    
    def countArrangement(self, N, arr=None):
        # 中文注释：如果未传入arr参数，则初始化为1到N的整数序列。
        # 英文注释: If no arr parameter is provided, initialize it as a sequence of integers from 1 to N.
        if not arr:
            arr = tuple(range(1, N + 1))
        
        # 中文注释：如果该问题已经计算过，或者N等于1，则直接返回结果。
        # 英文注释: If the problem has been calculated before or N equals 1, return the result directly.
        if (N, arr) in self.memo or N == 1:
            return N == 1 and 1 or self.memo[(N, arr)]
        
        # 中文注释：计算满足条件的排列数，并存储在memo字典中以备后续使用。
        # 英文注释: Calculate the number of valid arrangements that satisfy the condition, and store it in the memo dictionary for future use.
        self.memo[(N, arr)] = sum([
            self.countArrangement(N-1, arr[:j] + arr[j+1:]) 
            for j in range(len(arr)) if arr[j] % N == 0 or N % arr[j] == 0
        ])
        
        # 中文注释：返回计算结果。
        # 英文注释: Return the calculated result.
        return self.memo[(N, arr)]

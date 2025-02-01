
class Solution:
    # 判断列表A是否为单调的，即非递增或非递减
    def isMonotonic(self, A):
        # 检查元素顺序是否非递减
        non_decreasing = all(A[i] >= A[i - 1] for i in range(1, len(A)))
        
        # 检查元素顺序是否非递增
        non_increasing = all(A[i] <= A[i - 1] for i in range(1, len(A)))
        
        # 如果满足其中一个条件，则返回True，否则False
        return non_decreasing or non_increasing

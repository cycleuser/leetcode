
class Solution:
    # 定义一个方法来计算需要删除的最小列数，使得剩余的矩阵按行单调递增
    def minDeletionSize(self, A):
        # 计算所有列中存在非递增情况的数量
        return sum(any(a[j] > b[j] for a, b in zip(A, A[1:])) for j in range(len(A[0])))

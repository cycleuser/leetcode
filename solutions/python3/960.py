
class Solution:
    # 定义一个类来解决最小删除列数问题

    def minDeletionSize(self, A: list[str]) -> int:
        # 初始化行数m和列数n，分别代表矩阵A的长度和每个子列表的长度
        m, n = len(A), len(A[0])
        
        # dp数组初始化为1，表示每个列至少需要删除0次才能满足条件
        dp = [1] * n
        
        # 动态规划计算每一列是否可以通过前一列转换而来
        for j in range(1, n):
            for i in range(j):
                if all(A[k][i] <= A[k][j] for k in range(m)):
                    # 如果当前列的值大于等于所有行中对应上一个列的值，则更新dp[j]
                    dp[j] = max(dp[j], dp[i] + 1)
        
        # 返回需要删除的最小列数，即n减去可以保持递增的最长列数
        return n - max(dp)

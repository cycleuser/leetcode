
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int, mxTotal: float = -float("inf")) -> float:
        """
        寻找矩阵中和小于k的最大子矩阵的和。
        
        参数：
            matrix (List[List[int]]): 输入的二维整数数组
            k (int): 目标和
            mxTotal (float, 可选): 当前记录的最大和，默认为负无穷
        
        返回值：
            float: 符合条件的最大子矩阵和，若无符合条件的返回-无穷
        """
        for l in range(len(matrix[0])):
            # 初始化当前行的累加数组
            dp = [0] * len(matrix)
            for r in range(l, len(matrix[0])):
                # 从第l列到第r列计算每一行的累积和
                for i in range(len(matrix)):
                    dp[i] += matrix[i][r]
                
                # 初始化辅助数组及当前最大值
                sums, cur, mx = [float("inf")], 0, -float("inf")
                for sm in dp:
                    bisect.insort(sums, cur)
                    cur += sm
                    # 更新最大子矩阵和
                    mx = max(mx, cur - sums[bisect.bisect_left(sums, cur - k)])
                
                # 更新全局最大值
                mxTotal = max(mxTotal, mx)
        
        return mxTotal

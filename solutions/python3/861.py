
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        """
        类Solution包含一个方法matrixScore，用于计算矩阵A的分数。
        
        参数：
            A (List[List[int]]): 输入矩阵
        
        返回值：
            int: 矩阵A的最大可能分数
        """
        # 根据第一列调整行以优化初始分数
        for i, row in enumerate(A):
            if not row[0]:
                A[i] = [1 - num for num in row]
        
        m, n, sm = len(A), len(A and A[0]), 0
        
        # 计算每一列的最优值并累加到总分
        for c in range(n):
            cnt = sum(A[r][c] for r in range(m))
            sm += max(cnt, m - cnt) * 2 ** (n - c - 1)
        
        return sm

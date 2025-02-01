
class Solution:
    def largest1BorderedSquare(self, A: List[List[int]]) -> int:
        """
        分析：
            这个问题要求找到一个最大的只由1组成的正方形，并且该正方形的一边必须是其边界。
            通过构建两个辅助数组top和left来记录每个位置上方和左方连续1的数量，从而可以快速判断任意大小的正方形是否满足条件。

        :param A: List[List[int]] - 输入的二维数组
        :return: int - 最大只由1组成的正方形的面积
        """
        m, n = len(A), len(A[0])  # 获取矩阵的行数和列数
        res = 0  # 初始化结果，用于记录最大正方形边长

        top, left = [a[:] for a in A], [a[:] for a in A]  # 创建辅助数组top和left进行动态规划预处理

        # 动态规划填充top数组
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    if i: top[i][j] = top[i - 1][j] + 1
                    if j: left[i][j] = left[i][j - 1] + 1

        # 倒序遍历可能的正方形边长r
        for r in range(min(m, n), 0, -1):
            # 检查所有可能的左上角位置(i,j)
            for i in range(m - r + 1):
                for j in range(n - r + 1):
                    if min(top[i + r - 1][j], top[i + r - 1][j + r - 1], left[i]
                           [j + r - 1], left[i + r - 1][j + r - 1]) >= r:
                        return r * r  # 找到符合条件的正方形，直接返回其面积

        return 0  # 如果没有找到满足条件的正方形，则返回0

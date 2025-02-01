
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        """
        定义一个类来处理图像平滑操作
        
        :param M: 输入的二维整数数组，表示原始图像
        :return: 返回经过平滑处理后的二维数组
        """
        
        m, n = len(M), len(M[0])  # 获取矩阵的行数和列数
        grid = [[0] * n for _ in range(m)]  # 初始化结果矩阵
        
        # 遍历原始图像中的每一个像素点
        for i in range(m):
            for j in range(n):
                # 计算当前像素点及其邻域的有效像素值列表
                adj = [M[i + x][j + y] for x, y in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)) if 0 <= i + x < m and 0 <= j + y < n]
                # 将邻域平均值赋给结果矩阵中的对应位置
                grid[i][j] = sum(adj) // len(adj)
        
        return grid  # 返回处理后的图像矩阵


class Solution:
    # 定义一个计算矩阵最大矩形面积的方法
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        # 初始化结果，行数和列数变量
        res, m, n = 0, len(matrix), len(matrix and matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != "0":
                    # 如果当前位置不是“0”，则更新其值为左边连续1的数量加一
                    if j > 0 and matrix[i][j - 1] != "0":
                        matrix[i][j] = int(matrix[i][j - 1]) + 1
                    else:
                        matrix[i][j] = 1
                    
                    # 记录当前元素值，用于后续计算矩形高度
                    mn, sm, k = matrix[i][j], 0, i + 1
                    
                    while k > 0 and matrix[k - 1][j] != "0":
                        if matrix[k - 1][j] < mn:
                            # 更新最小高度和面积
                            sm, mn = (i - k + 2) * int(matrix[k - 1][j]), int(matrix[k - 1][j])
                        else:
                            # 累加当前行的矩形面积
                            sm += mn
                        
                        if sm > res:
                            # 更新最大矩形面积
                            res = sm
                        k -= 1
        
        return res

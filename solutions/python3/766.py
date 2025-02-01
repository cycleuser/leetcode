
class Solution:
    # 判断给定矩阵是否为托普利茨矩阵，即除了主对角线元素外的每个元素都等于其左上方元素
    def isToeplitzMatrix(self, matrix):
        # 使用all函数和生成器表达式来检查矩阵中每个元素是否满足托普利茨矩阵条件
        return all(matrix[i][j] == matrix[i - 1][j - 1] for i in range(1, len(matrix)) for j in range(1, len(matrix[0])))


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """
        计算在矩阵中通过翻转行操作可以使得相同的最大行数。

        :param matrix: 二维整数列表，表示输入的矩阵
        :return: 在进行翻转操作后，最多有多少行是相同的
        """

        res = 0
        # 遍历每一行
        for row in matrix:
            # 获取当前行的反向序列
            inv = [1 - r for r in row]
            # 检查当前行及其反转行在矩阵中出现的次数，并更新最大值
            res = max(res, sum(row == r or inv == r for r in matrix))
        return res


class Solution:
    # 获取第 rowIndex 行的杨辉三角形行，使用递归实现
    def getRow(self, rowIndex: int, row = [1]) -> List[int]:
        # 如果当前层级为 0，则直接返回初始行 [1]
        if not rowIndex:
            return row

        # 否则，通过计算上一行的相邻元素和生成新行
        # 在列表推导式中使用 zip 函数将两个扩展后的列表合并，并进行累加操作
        return self.getRow(rowIndex - 1, [a + b for a, b in zip([0] + row, row + [0])])

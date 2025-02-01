
class Solution:
    # 解决方案类

    def countCornerRectangles(self, grid):
        # 计算网格中角落矩形的数量
        
        from collections import defaultdict
        # 导入字典默认值初始化功能
        
        ends, res = defaultdict(int), 0
        # 初始化计数器ends和结果res
        
        for row in grid:
            # 遍历每一行
            for i in range(len(row) - 1):
                # 遍历该行的前半部分，i从0到len(row)-2
                for j in range(i + 1, len(row)):
                    # 遍历以j为结束点的后半部分，确保与i不重复
                    if row[i] and row[j]:
                        # 判断row[i]和row[j]是否都为True
                        ends[(i, j)] = ends.get((i, j), 0) + 1
                        # 更新ends字典中(i,j)的计数
                        res += ends[(i, j)] - 1
                        # 累加以(i,j)结尾的矩形数量，减1是因为(i,j)自身不是完整的角落矩形
        return res
        # 返回结果res

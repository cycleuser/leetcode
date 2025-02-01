
class Solution:
    # 定义解决方案类

    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> list[list[int]]:
        # 初始化方向、结果列表、总节点数、步长和当前方向索引
        direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        res = [[r0, c0]]
        n = R * C
        l, ind = 1, 1
        
        # 当结果列表长度小于总节点数时，继续生成螺旋矩阵
        while len(res) < n:
            for _ in range(2):  # 每层循环两次（水平+垂直）
                for __ in range(l):
                    r0 += direct[ind][0]
                    c0 += direct[ind][1]  # 更新当前位置坐标
                    if 0 <= r0 < R and 0 <= c0 < C:  # 判断是否在矩阵范围内
                        res.append([r0, c0])
                ind = (ind + 1) % 4  # 更换方向索引
            l += 1  # 增加步长

        return res  # 返回结果列表

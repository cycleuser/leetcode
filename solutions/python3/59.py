
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        :type n: int
        :rtype: List[List[int]]
        
        生成一个 n x n 的矩阵，按照螺旋顺序填充数字1到n*n。
        """

        def dirToIndex(x: int, y: int, d: str) -> Tuple[int, int, str]:
            """
            根据当前方向d计算下一个位置和新方向
            :param x: 当前行索引
            :param y: 当前列索引
            :param d: 当前方向，r(右), d(下), l(左), u(上)
            :return: (new_x, new_y, new_direction)
            """
            if d == "r":
                return (x, y + 1, d) if y + 1 < n and matrix[x][y + 1] == 0 else (x + 1, y, "d")
            elif d == "d":
                return (x + 1, y, d) if x + 1 < n and matrix[x + 1][y] == 0 else (x, y - 1, "l")
            elif d == "l":
                return (x, y - 1, d) if y > 0 and matrix[x][y - 1] == 0 else (x - 1, y, "u")
            else:
                return (x - 1, y, d) if x > 0 and matrix[x - 1][y] == 0 else (x, y + 1, "r")

        # 初始化矩阵
        matrix = [[0 for i in range(n)] for j in range(n)]
        
        num, dir, i, j = 1, "r", 0, 0
        
        # 按照螺旋顺序填充数字
        while 0 <= i < n and 0 <= j < n and matrix[i][j] == 0:
            matrix[i][j] = num
            num += 1
            i, j, dir = dirToIndex(i, j, dir)

        return matrix

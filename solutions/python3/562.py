
class Solution:
    # 定义一个类来解决问题

    def longestLine(self, M):
        # 初始化四个方向的最大连续线数字典，以及最大值变量mx、矩阵的行数m和列数n
        hor, ver, dig, aDig, mx, m, n = {}, {}, {}, {}, 0, len(M), len(M and M[0])

        for i in range(m):
            # 遍历每一行
            for j in range(n):
                # 如果当前位置为1（表示存在线）
                if M[i][j]:
                    # 更新竖直方向的最大连续线数
                    ver[(i, j)] = (ver.get((i, j - 1), 0) + 1) if j > 0 and M[i][j - 1] else 1

                    # 更新水平方向的最大连续线数
                    hor[(i, j)] = (hor.get((i - 1, j), 0) + 1) if i > 0 and M[i - 1][j] else 1

                    # 更新主对角线方向的最大连续线数
                    dig[(i, j)] = (dig.get((i - 1, j - 1), 0) + 1) if i > 0 and j > 0 and M[i - 1][j - 1] else 1

                    # 更新副对角线方向的最大连续线数
                    aDig[(i, j)] = (aDig.get((i - 1, j + 1), 0) + 1) if i > 0 and j + 1 < n and M[i - 1][j + 1] else 1

                    # 更新最大值mx
                    mx = max(mx, ver[(i, j)], hor[(i, j)], dig[(i, j)], aDig[(i, j)])

        return mx

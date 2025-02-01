
class Solution:
    # 定义一个解题类

    def wallsAndGates(self, rooms):
        m, n = len(rooms), len(rooms[0])  # 获取房间网格的行数和列数
        # 初始化队列和距离变量，将所有门的位置加入初始队列，并设置起始距离为0
        q, dist = [(i, j) for i in range(m) for j in range(n) if not rooms[i][j]], 0

        while q:
            new = []
            # 每次循环增加一次距离
            dist += 1
            for i, j in q:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2147483647:
                        # 如果找到新的未访问过的房间，更新其距离并加入队列
                        rooms[x][y] = dist
                        new.append((x, y))
            q = new  # 更新当前待处理的房间列表

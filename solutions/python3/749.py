
class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 如果grid为空，返回None
        if not grid: 
            return None
        
        N, M = len(grid), len(grid[0])  # 获取grid的行数和列数

        def around(r, c, t=None):
            """
            返回所有距离为1的单元格坐标
            如果t不为空，只返回值等于t的单元格坐标
            :param r: 当前行索引
            :param c: 当前列索引
            :param t: 目标值
            :return: 所有可能的相邻单元格坐标
            """
            for d in (-1, 1):
                for (rr, cc) in ((r + d, c), (r, c + d)):
                    if 0 <= rr < N and 0 <= cc < M and (t == None or grid[rr][cc] == t):
                        yield (rr, cc)

        def regions():
            """
            返回所有区域
            :return: 区域列表
            """
            regs = []
            seen = set()
            for r in range(N):
                for c in range(M):
                    if grid[r][c] == 1 and (r, c) not in seen:
                        # 新发现的区域，进行BFS遍历
                        reg = set()
                        front, newfront = [(r, c)], []
                        while front:
                            reg.update(front)
                            while front:
                                (rr, cc) = front.pop()
                                for (rr, cc) in around(rr, cc, 1):
                                    if (rr, cc) not in reg:
                                        newfront.append((rr, cc))
                                        reg.add((rr, cc))
                            front, newfront = newfront, front
                        regs.append(reg)
                        seen.update(reg)
            return regs

        def reg_boundary(reg):
            """
            返回给定区域的边界单元格集合
            :param reg: 区域
            :return: 边界单元格集合
            """
            bound = set()
            for (r, c) in reg:
                for (rr, cc) in around(r, c, 0):
                    bound.add((rr, cc))
            return bound

        def reg_walls(reg, bound):
            """
            返回将给定区域隔离所需的墙壁数量
            :param reg: 区域
            :param bound: 边界单元格集合
            :return: 墙壁数量
            """
            walls = 0
            for (r, c) in bound:
                for (rr, cc) in around(r, c, 1):
                    if (rr, cc) in reg:
                        walls += 1
            return walls

        gwalls = 0

        while True:

            regs = regions()

            if not regs: 
                break
            # 找出边界最大的区域
            reg = max(regs, key=lambda reg: len(reg_boundary(reg)))
            walls = reg_walls(reg, reg_boundary(reg))
            gwalls += walls

            # 将选定区域标记为隔离
            for (r, c) in reg:
                grid[r][c] = 2

            # 计算新的感染传播情况
            infected = set()
            for r in range(N):
                for c in range(M):
                    if grid[r][c] == 1:
                        for (rr, cc) in around(r, c, 0):
                            infected.add((rr, cc))

            # 更新grid，让新感染的区域变为活跃
            for r, c in infected:
                grid[r][c] = 1

            if not infected: 
                break
        
        return gwalls

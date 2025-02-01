
class Solution:

    def __init__(self, rects):
        """
        初始化类实例，设置矩形区域，并计算累积范围。
        
        :param rects: 输入的矩形区域列表
        """
        self.rects, self.ranges, sm = rects, [], 0
        for x1, y1, x2, y2 in rects:
            # 计算每个矩形面积并累加到总和中，用于后续随机选择
            sm += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(sm)

    def pick(self):
        """
        随机选择一个点从给定的矩形区域中。

        :return: 返回在某个矩形中的随机坐标
        """
        idx = bisect.bisect_left(self.ranges, random.randint(1, self.ranges[-1]))
        # 通过累积范围找到对应的矩形
        x1, y1, x2, y2 = self.rects[idx]
        # 返回该矩形中的随机点坐标
        return [random.randint(x1, x2), random.randint(y1, y2)]

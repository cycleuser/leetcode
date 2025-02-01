
class Solution:
    def isReflected(self, points):
        """
        判断给定点集是否关于某条直线对称。

        参数:
        points: List[Tuple[int, int]], 点的集合

        返回:
        bool, 如果点集关于某条直线对称则返回 True，否则返回 False
        """

        if len(points) < 2:
            return True  # 如果点的数量少于2，则直接返回True，因为不可能不对称

        # 计算所有x坐标的中位线
        x = (min(x for x, y in points) + max(x for x, y in points)) / 2 

        left_set, right_set, on_line_set = set(), set(), set()
        for i, j in points:
            if i < x:  # 点位于中位线左边
                left_set.add((i, j))
            elif i > x:  # 点位于中位线右边
                right_set.add((i, j))
            else:  # 点在中位线上
                on_line_set.add((i, j))

        for i, j in points:
            if i < x and (2 * x - i, j) in right_set:  # 检查左边点的对称点是否在右边集合中
                continue
            elif i > x and (2 * x - i, j) in left_set:  # 检查右边点的对称点是否在左边集合中
                continue
            elif i == x and (2 * x - i, j) in on_line_set:  # 检查中位线上点的对称点是否也在中位线集合中
                continue
            else:
                return False

        return True

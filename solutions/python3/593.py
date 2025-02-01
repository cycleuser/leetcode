
class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        """
        判断四个点是否能构成一个非退化的正方形。
        
        :param p1: 第一个点的坐标
        :param p2: 第二个点的坐标
        :param p3: 第三个点的坐标
        :param p4: 第四个点的坐标
        :return: 如果可以构成非退化的正方形返回True，否则返回False
        
        1. 计算每对点之间的距离平方。
        2. 集合存储这些距离平方。
        3. 判断集合长度是否为2且包含0的情况不存在。
        """
        from itertools import combinations as cb

        def distance_squared(coord1, coord2):
            """
            计算两个坐标之间的距离的平方。

            :param coord1: 第一个坐标的元组形式 (x, y)
            :param coord2: 第二个坐标的元组形式 (x, y)
            :return: 两点间距离的平方
            """
            return (coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2

        # 计算所有点对的距离平方并去重
        distances = set(map(lambda pair: distance_squared(pair), cb([p1, p2, p3, p4], 2)))
        
        # 检查条件：必须有两个不同的距离且没有长度为0的情况（三点共线）
        return len(distances) == 2 and 0 not in distances

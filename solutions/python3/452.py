
class Solution:
    def findMinArrowShots(self, points):
        """
        输入：points - 覆盖目标的气球位置列表，每个元素表示一个区间 [x_start, x_end]。
        
        输出：最少需要多少支箭才能射破所有气球。
        """
        # 按照每个区间的结束位置排序
        points.sort(key=lambda x: x[1])
        
        if not points:
            return 0
        
        # 初始化结果和当前箭的位置
        res = 1  # 至少需要一支箭
        curr = points[0][1]
        
        for point in points:
            # 如果当前气球的起始位置大于当前箭的位置，则需要额外一支箭，并更新箭的位置为当前区间的结束位置
            if point[0] > curr:
                res, curr = res + 1, point[1]
        
        return res

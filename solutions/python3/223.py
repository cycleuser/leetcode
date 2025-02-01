
class Solution:
    # 计算矩形的交集面积

    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # 计算每个矩形的宽度和高度
        width_a = abs(ax1 - ax2)
        height_a = abs(ay1 - ay2)
        width_b = abs(bx1 - bx2)
        height_b = abs(by1 - by2)

        # 计算重叠部分的宽度和高度
        overlap_width = max(min(ax2, bx2) - max(ax1, bx1), 0)
        overlap_height = max(min(ay2, by2) - max(ay1, by1), 0)

        # 如果没有重叠，交集面积为0
        intersection_area = overlap_width * overlap_height if overlap_width > 0 and overlap_height > 0 else 0

        # 总面积减去交集面积得到不重叠部分的面积
        return width_a * height_a + width_b * height_b - intersection_area


class Solution:
    # 检查点是否在同一直线上

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # 计算每两个连续点的斜率，如果所有斜率都相等，则这些点在同一条直线上
        return len(set((b[1] - a[1]) / (b[0] - a[0]) if b[0] != a[0] else float('inf') for a, b in zip(coordinates, coordinates[1:]))) == 1

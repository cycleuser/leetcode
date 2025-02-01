
class Solution:
    # 定义一个类，用于解决公交车站之间的距离问题

    def distanceBetweenBusStops(self, d: List[int], i: int, j: int) -> int:
        # 计算两段路径的距离之和，并返回较小的那个值
        
        # 中文注释：计算两个公交站点i和j之间较短的路径长度
        return min(
            sum(d[min(i, j):max(i, j)]),  # 从较小索引到较大索引之间的距离
            sum(d[:min(i, j)] + d[max(i, j):])  # 分段计算，包括两端
        )

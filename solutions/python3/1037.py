
class Solution:
    # 检查三个点是否能组成一个boomerang（非共线）
    def isBoomerang(self, p: List[List[int]]) -> bool:
        return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1])

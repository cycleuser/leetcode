
class Solution:
    # 判断一个点集是否为凸多边形
    def isConvex(self, points):
        # 计算向量方向，用于判断点的方向性
        def direction(a, b, c): 
            return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        
        d, n = 0, len(points)
        # 遍历点集，检查相邻三点的方向性是否一致
        for i in range(n):
            a = direction(points[i], points[(i + 1) % n], points[(i + 2) % n])
            if not d: 
                d = a
            elif a * d < 0:
                return False
        
        return True

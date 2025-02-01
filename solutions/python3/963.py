
class Solution:
    # 定义一个类来解决最小自由矩形面积问题

    def minAreaFreeRect(self, points):
        # 初始化最小面积为正无穷大，存储所有点的集合，并获取点的数量
        mn, st, n = float('inf'), {(x, y) for x, y in points}, len(points)
        
        # 遍历每一个顶点i
        for i in range(n):
            x1, y1 = points[i]
            
            # 从i之后的每个顶点j开始，避免重复计算
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                # 从j之后的每个顶点k开始，形成一个矩形的三条边
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    
                    # 检查是否能构成直角三角形（即第三条边与前两条垂直）
                    if not (x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1):
                        # 确认第四点存在
                        if (x3 + (x2 - x1), y3 + (y2 - y1)) in st:
                            # 计算矩形的面积并更新最小值
                            mn = min(mn, ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 * ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5)
        
        # 如果找到了有效矩形，返回最小面积；否则返回0
        return mn if mn < float("inf") else 0

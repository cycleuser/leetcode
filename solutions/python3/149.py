
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # 计算两点之间的斜率，或者判断为垂直线
    def maxPoints(self, points):
        m, res, roots = {}, 0, set()  # 初始化存储斜率的字典、最大点数和已访问点集
        
        for i, p1 in enumerate(points):  # 遍历每个点p1
            if (p1.x, p1.y) not in roots:  # 如果该点未被访问过
                roots.add((p1.x, p1.y))  # 标记为已访问
                m.clear()  # 清空字典，重新计算斜率
                dup = path = 0  # 初始化重复点数和路径最大长度
                
                for j, p2 in enumerate(points):  # 遍历每个点p2
                    if i != j:  # 确保不与自身比较
                        try:
                            cur = (p1.y - p2.y) * 100 / (p1.x - p2.x)  # 计算斜率，乘以100避免精度问题
                        except ZeroDivisionError:
                            if p1.y == p2.y:  # 如果两点纵坐标相同，则为重复点
                                dup += 1
                                continue
                            else:
                                cur = "ver"  # 垂直线标记为"ver"
                        
                        m[cur] = m.get(cur, 0) + 1  # 更新斜率计数
                        if m[cur] > path:  # 更新路径最大长度
                            path = m[cur]
                
                # 计算当前路径下的最大点数，并更新全局结果
                if path + dup + 1 > res:
                    res = path + dup + 1
        
        return res  # 返回最终的最大点数

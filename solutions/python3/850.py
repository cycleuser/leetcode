
class Solution:
    def rectangleArea(self, rectangles):
        # 获取所有x轴边界点并排序去重
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]] + [0]))
        
        # 构建x坐标到索引的映射
        x_i = {v: i for i, v in enumerate(xs)}
        
        # 初始化计数数组，记录每个区间的状态变化
        count = [0] * len(x_i)
        
        # 记录所有边界点事件
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, x1, x2, 1])  # 左边界进入
            L.append([y2, x1, x2, -1])  # 右边界退出
        
        # 按纵坐标排序事件列表，确保按顺序处理矩形的上下边界
        L.sort()
        
        # 当前纵坐标和当前横坐标和面积
        cur_y = cur_x_sum = area = 0
        
        # 遍历所有事件点进行计算
        for y, x1, x2, sig in L:
            # 计算新增的面积并累加
            area += (y - cur_y) * cur_x_sum
            
            # 更新当前纵坐标
            cur_y = y
            
            # 根据矩形边界更新计数数组状态
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sig
            
            # 重新计算当前横坐标的总和，过滤掉消失的区间
            cur_x_sum = sum((x2 - x1) if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
        
        return area % (10 ** 9 + 7)

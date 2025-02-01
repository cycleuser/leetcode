
class Solution:
    # 判断给定的矩形集合是否能完全覆盖一个大矩形
    
    def isRectangleCover(self, rectangles):
        from collections import Counter
        
        # 使用计数器统计每个顶点出现次数
        cnt = Counter()
        for x1, y1, x2, y2 in rectangles:
            cnt[(x1, y1)] += 1
            cnt[(x1, y2)] += 1
            cnt[(x2, y2)] += 1
            cnt[(x2, y1)] += 1
        
        # 计算大矩形的左下角和右上角坐标
        x1, y1 = min([r[:2] for r in rectangles])
        x2, y2 = max(r[-2:] for r in rectangles)
        
        # 检查四个顶点是否各出现一次
        for (x, y) in ((x1, y1), (x1, y2), (x2, y2), (x2, y1)):
            if cnt[(x, y)] != 1:
                return False
            cnt.pop((x, y))
        
        # 检查其他顶点是否符合预期
        return all(cnt[k] in (2, 4) for k in cnt) and \
               sum((x2 - x1) * (y2 - y1) for x1, y1, x2, y2 in rectangles) == (x2 - x1) * (y2 - y1)


class Solution:
    """
    解决最小矩形面积问题。
    
    Class to solve the problem of finding the minimum area of a rectangle.
    """

    def minAreaRect(self, points):
        """
        计算给定点集合中最小的矩形面积。

        Calculate the minimum area of a rectangle from the given set of points.
        
        :param points: 列表，包含点集 (x, y)。
        :type points: List[List[int]]
        :return: 最小矩形面积
        :rtype: int
        """
        seen, bases, baseX, res = collections.defaultdict(dict), [], -1, float("inf")
        
        # 对 x 坐标进行排序，便于后续处理
        for x, y in sorted(points):
            if x != baseX:
                # 更新 baseX 并清空 bases 列表
                baseX, bases = x, []
            
            # 遍历当前横坐标下的所有基线
            for base in bases:
                # 如果存在 y 值相同的点，则计算矩形面积并更新最小值
                if y in seen[base]:
                    res = min(res, (x - seen[base][y]) * (y - base))
                
                # 记录当前 x 坐标下的基线 y 值
                seen[base][y] = x
            
            # 将当前 y 值添加到 bases 列表中，用于后续比较
            bases.append(y)
        
        return res if res < float("inf") else 0

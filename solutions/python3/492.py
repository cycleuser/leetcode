
class Solution:
    def constructRectangle(self, area):
        """
        :type area: int  # 输入参数area，表示矩形的面积
        :rtype: List[int]  # 返回一个列表，包含构造矩形的长和宽
        """
        import math
        l, w = int(math.sqrt(area)), int(math.sqrt(area))  # 初始化长和宽为平方根值
        
        while l * w != area:  # 当长乘以宽不等于面积时循环
            if area % w == 0:  # 如果宽度w可以整除面积，则更新长度l
                l = int(area / w)
            else:
                w -= 1  # 否则减小宽度直到找到合适的尺寸
        
        return [l, w]  # 返回构造的长和宽

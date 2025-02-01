    
class Solution:
    """
    判断两个矩形是否重叠

    通过检查两个矩形在x轴和y轴上的投影是否相互交错来判断。
    """

    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # 检查矩形的左边界与右边界是否交错
        x_overlap = (rec1[2] - rec1[0] + rec2[2] - rec2[0]) > (max(rec1[2], rec2[2]) - min(rec1[0], rec2[0]))
        
        # 检查矩形的下边界与上边界是否交错
        y_overlap = (rec1[3] - rec1[1] + rec2[3] - rec2[1]) > (max(rec1[3], rec2[3]) - min(rec1[1], rec2[1]))
        
        # 两个方向都需交错，矩形才重叠
        return x_overlap and y_overlap

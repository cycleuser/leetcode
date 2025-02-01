
class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        """
        判断路径是否会自相交
        
        参数:
            x (List[int]): 路径的长度列表
        
        返回:
            bool: 如果路径会自相交返回True，否则返回False
        """
        b = c = d = e = 0
        for a in x:
            # 判断当前段是否会与前一段发生交叉
            if d >= b > 0 and (a >= c or a >= c - e >= 0 and f >= d - b):
                return True
            # 更新变量
            b, c, d, e, f = a, b, c, d, e
        return False

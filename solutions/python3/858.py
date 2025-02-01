
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        解决问题：模拟光束在镜子上的反射路径，返回光束最终所在的位置。
        
        参数：
            p (int): 镜子的垂直边长
            q (int): 光源与垂直边的距离
        
        返回值：
            int: 光束最终所在的角编号（0, 1, 或 2）
        """
        side, up, h = 2, 1, 0  # 初始化：side表示水平方向的位置，up表示垂直方向的移动方向，h表示当前高度
        while True:
            h += q * up  # 更新光束的高度
            side = (side + 1) % 2  # 水平方向翻转
            if side == 0:
                side += 2  # 如果在最左面，恢复为初始状态
            if h < 0:
                h *= -1  # 翻转光束垂直方向
                up *= -1
            elif h > p:
                h = p - (h - p)  # 碰到上边，调整高度并翻转方向
                up *= -1
            if h % p == 0:  # 判断是否到达底部或顶部
                return h and side or 0  # 返回光束所在的位置

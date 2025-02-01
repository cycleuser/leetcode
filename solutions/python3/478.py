
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        """
        初始化圆的中心坐标和半径。
        :param radius: 圆的半径，float 类型
        :param x_center: 圆心在 x 轴上的坐标，float 类型
        :param y_center: 圆心在 y 轴上的坐标，float 类型
        """
        self.x = x_center  # 圆心横坐标
        self.y = y_center  # 圆心纵坐标
        self.r = radius    # 圆的半径

    def randPoint(self) -> List[float]:
        """
        随机生成圆内的一点。
        :return: 返回一个包含两个 float 值的列表，表示随机点的坐标 (x, y)
        """
        r, angle, scale = random.uniform(0, self.r), random.uniform(0, 2 * math.pi), math.sqrt(random.uniform(0, 1))
        return [self.x + self.r * scale * math.cos(angle), self.y + self.r * scale * math.sin(angle)]

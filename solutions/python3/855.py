
class ExamRoom:

    # 初始化教室座位数量N，seated记录当前已占用的座位索引列表
    def __init__(self, N: int):
        self.seated, self.n = [], N - 1

    # 选择一个最远距离的位置就座
    def seat(self) -> int:
        if not self.seated:
            self.seated += [0],  # 空列表添加元素需要逗号，表示单个元素的元组
            return 0

        mx, ind = 0, 0  # 最大距离和对应的索引位置初始化

        # 遍历已占用座位，计算空位最大距离
        for i in range(1, len(self.seated)):
            l, r = self.seated[i - 1], self.seated[i]
            if (r - l) // 2 > mx:
                mx, ind = (r - l) // 2, l + mx

        # 检查两端空位情况
        if self.seated[-1] != self.n and self.n - self.seated[-1] > mx:
            mx, ind = self.n - self.seated[-1], self.n

        if self.seated[0] >= mx:
            mx, ind = self.seated[0], 0

        # 就座
        self.seated.append(ind)
        self.seated.sort()
        return ind

    # 离开座位，更新已占用的座位列表
    def leave(self, p: int):
        self.seated.remove(p)

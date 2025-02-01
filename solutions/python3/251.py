
class Vector2D:
    # 构造函数，初始化二维向量的数组和指针位置
    def __init__(self, v: List[List[int]]):
        self.arr = v  # 存储输入的二维数组
        self.rows = len(v)  # 获取行数
        self.i = self.j = 0  # 初始化索引i和j

    def next(self) -> int:
        # 返回下一个元素并移动指针
        if self.hasNext():
            self.j += 1  # 移动列指针
            return self.arr[self.i][self.j - 1]  # 返回当前元素

    def hasNext(self) -> bool:
        # 判断是否有下一个元素
        if self.arr and self.j == len(self.arr[self.i]):  # 当前行已遍历完，移动到下一行
            self.i += 1
            self.j = 0
        while self.i + 1 < self.rows and not self.arr[self.i]:  # 跳过空行
            self.i += 1
        return self.i < self.rows and self.arr[self.i] != []  # 判断是否还有元素可遍历

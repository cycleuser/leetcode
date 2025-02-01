
import random

class RandomizedCollection:

    # 初始化，使用列表存储元素和一个字典存储每个元素的位置集合
    def __init__(self):
        self.arr, self.pos = [], collections.defaultdict(set)

    # 插入元素，返回插入后该值在集合中的唯一性状态
    def insert(self, val: int) -> bool:
        out = val not in self.pos  # 判断插入前该值是否已存在
        self.arr.append(val)
        self.pos[val].add(len(self.arr) - 1)  # 更新位置字典
        return out

    # 移除元素，返回移除操作是否成功
    def remove(self, val: int) -> bool:
        if val in self.pos:
            if self.arr[-1] != val:
                x, y = self.pos[val].pop(), self.arr[-1]
                self.pos[y].discard(len(self.arr) - 1)
                self.pos[y].add(x)
                self.arr[x] = y
            else:
                self.pos[val].discard(len(self.arr) - 1)
            self.arr.pop()  # 移除最后一个元素
            if not self.pos[val]:
                self.pos.pop(val)
            return True 
        return False

    # 随机获取一个元素
    def getRandom(self):
        return random.choice(self.arr)

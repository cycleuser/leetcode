
class MyHashMap:

    # 构造函数，初始化一个大小为1000001的数组，初始值均为-1
    def __init__(self):
        self.arr = [-1] * 1000001

    # 向哈希表中插入或更新键值对
    def put(self, key: int, value: int) -> None:
        self.arr[key] = value

    # 根据键获取对应的值，如果不存在则返回-1
    def get(self, key: int) -> int:
        return self.arr[key]

    # 移除哈希表中指定的键及其对应的值
    def remove(self, key: int) -> None:
        self.arr[key] = -1

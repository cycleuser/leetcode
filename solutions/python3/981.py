
class TimeMap:

    # 构造函数，初始化两个字典，默认值为列表
    def __init__(self):
        from collections import defaultdict
        self.times = defaultdict(list)   # 存储时间戳
        self.values = defaultdict(list)  # 存储对应的值

    # 设置键的值和对应的时间戳
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)  # 将时间戳添加到对应键的列表中
        self.values[key].append(value)     # 将值添加到对应键的列表中

    # 获取特定键在某个时间戳之前的最大值
    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)  # 使用二分查找找到插入位置
        return self.values[key][i - 1] if i else ''   # 如果找到了，则返回对应的值，否则返回空字符串

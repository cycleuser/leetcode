
class PhoneDirectory:

    # 初始化电话目录，设置最大号码数量
    def __init__(self, maxNumbers: int):
        self.nums = set(range(maxNumbers))  # 使用集合存储可用号码

    # 获取一个未使用的号码并将其从集合中移除
    def get(self) -> int:
        return self.nums.pop() if self.nums else -1  # 返回一个号码，如果无号码则返回-1

    # 检查给定的号码是否可用
    def check(self, number: int) -> bool:
        return number in self.nums  # 如果号码在集合中，则表示可用

    # 释放指定的号码使其再次可用
    def release(self, number: int):
        self.nums.add(number)  # 将号码添加回集合

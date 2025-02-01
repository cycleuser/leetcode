
class TwoSum:

    # 初始化类，使用字典存储数字及其出现次数
    def __init__(self):
        self.nums = {}

    # 添加一个数到集合中，同时更新其出现次数
    def add(self, number: int) -> None:
        self.nums[number] = self.nums.get(number, 0) + 1

    # 检查是否存在两个数之和等于给定值
    def find(self, value: int) -> bool:
        for num in self.nums:
            if (value - num in self.nums and 
                (num != value - num or self.nums[num] > 1)):
                return True
        return False

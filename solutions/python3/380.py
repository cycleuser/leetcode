
import random

class RandomizedSet:

    def __init__(self):
        """
        初始化数据结构。
        Initialize the data structure.
        """
        self.nums, self.ind = [], {}

    def insert(self, val):
        """
        向集合中插入一个值。如果集合未包含该元素，则返回 true；否则，返回 false。
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.ind:
            self.nums.append(val)  # 使用 append 更简洁
            self.ind[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        """
        从集合中移除一个值。如果集合包含该元素，则返回 true；否则，返回 false。
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ind:
            ind, last = self.ind[val], self.nums[-1]
            self.nums[ind] = last  # 用最后一个元素替换目标元素
            self.ind[last] = ind   # 更新索引字典
            self.nums.pop()        # 移除最后一个元素（现在变成了被移除的元素）
            self.ind.pop(val)
            return True
        return False

    def getRandom(self):
        """
        从集合中随机获取一个元素。
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

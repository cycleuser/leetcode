
class Solution:

    def __init__(self, nums):  # 初始化类，传入一个整数列表
        """
        :param nums: 初始的整数列表
        """
        self.indexes = collections.defaultdict(set)  # 使用字典存储每个数字及其索引集合
        for i, num in enumerate(nums):
            self.indexes[num].add(i)  # 将当前索引添加到对应数字的集合中

    def pick(self, target):  # 根据目标值返回一个随机索引
        """
        :param target: 目标整数
        :return: 返回一个随机选择的目标值对应的索引，保证该索引存在于字典中的目标值集合中
        """
        return random.sample(self.indexes[target], 1)[0]  # 使用random.sample从目标值的索引集合中随机选取一个

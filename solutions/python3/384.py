
class Solution:

    def __init__(self, nums: List[int]):
        """
        初始化时复制输入数组作为原始配置，并存储在self.org中。
        同时，将输入数组复制一份保存在self.arr中用于后续操作。
        :param nums: 输入整数列表
        """
        self.arr = nums
        self.org = nums[:]

    def reset(self) -> List[int]:
        """
        将数组恢复到原始配置并返回。
        这相当于撤销所有已执行的洗牌操作，使其回到初始状态。
        :return: 返回重置后的数组
        """
        self.arr = self.org[:]
        return self.arr

    def shuffle(self) -> List[int]:
        """
        随机打乱数组中的元素顺序并返回打乱后的数组。
        使用random.shuffle方法实现随机化操作。
        :return: 返回打乱后的数组
        """
        random.shuffle(self.arr)
        return self.arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

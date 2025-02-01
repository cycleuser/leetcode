
class KthLargest(object):

    def __init__(self, k, nums):
        """
        初始化KthLargest类，使用一个小顶堆来维护前k大的元素。

        :param k: int - 表示要找到的第k大元素的位置。
        :param nums: List[int] - 初始的数字列表。
        """
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)  # 将列表转换为小顶堆
        while len(self.pool) > k:
            heapq.heappop(self.pool)  # 弹出最小值，保持堆中只有k个元素

    def add(self, val):
        """
        添加一个新值到KthLargest对象中，并返回当前第k大元素。

        :param val: int - 要添加的数值。
        :return: int - 当前堆中的第k大元素。
        """
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)  # 堆中元素小于k时直接插入
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)  # 如果新值大于堆顶，用新值替换堆顶并返回旧堆顶
        return self.pool[0]


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        不返回任何内容，而是就地修改nums。
        """

        # 将数组中的元素取负值，并构建最小堆
        heap = [-num for num in nums]
        heapq.heapify(heap)

        # 交替填充奇数索引位置（1, 3, 5...），从堆顶弹出最大值
        for i in range(1, len(nums), 2):
            nums[i] = -heapq.heappop(heap)

        # 交替填充偶数索引位置（0, 2, 4...），从堆顶弹出最大值
        for i in range(0, len(nums), 2):
            nums[i] = -heapq.heappop(heap)

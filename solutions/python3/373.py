
class Solution:
    # 定义一个类，用于解决求两个数组中和最小的k对值的问题

    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        """
        :param nums1: 第一个整数列表
        :param nums2: 第二个整数列表
        :param k: 最小的k对值
        :return: 返回最小和的前k对值组成的列表，每一对为两个整数组成的小列表

        1. 检查输入是否有空数组
        2. 初始化变量n表示nums2长度，res用于存储结果，cnt计数器，heap用作优先队列
        3. 将nums1中的每个元素与nums2的第一个元素组合放入堆中
        4. 循环直到找到k对最小值或堆为空：
           - 弹出堆顶元素，增加计数器
           - 如果当前索引未超出边界，则将新的组合加入堆中
           - 将当前最小和的两个整数加入结果列表
        """
        if not nums1 or not nums2:
            return []

        n, res, cnt, heap = len(nums2), [], 0, [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]

        while heap and cnt < k:
            cnt += 1
            sm, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n: heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res


class Solution:
    # 定义一个类，用于解决最大子数组和的问题

    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :param nums: List[int] - 输入的整数列表
        :param k: int - 子数组的长度
        :return: List[int] - 三个具有最大总和的子数组的起始索引

        思路：
        使用滑动窗口技术，首先计算每个可能子数组的和。
        然后遍历这些子数组来找到最优解。
        """
        single, double, sm, n, cur = {}, {}, 0, len(nums), sum(nums[:k - 1])
        # 初始化单个子数组和双个子数组字典，当前窗口总和，数组长度以及初始窗口总和

        for i in range(k - 1, n):
            cur += nums[i]
            single[i - k + 1] = cur
            cur -= nums[i - k + 1]
        # 遍历计算每个可能子数组的和并存储在字典中

        cur = (n - k), single[n - k]
        for i in range(n - k, k * 2 - 1, -1):
            if single[i] >= cur[1]:
                cur = i, single[i]
            double[i - k] = (cur[1] + single[i - k], i - k, cur[0])
        # 遍历计算每个可能双个子数组的和并存储在字典中

        cur = double[n - 2 * k]
        for i in range(n - 2 * k, k - 1, -1):
            if double[i][0] >= cur[0]:
                cur = double[i]
            if single[i - k] + cur[0] >= sm:
                sm, res = single[i - k] + cur[0], [i - k, cur[1], cur[2]]
        # 遍历计算最终的最优解
        return res

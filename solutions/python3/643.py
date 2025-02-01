
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """
        :param nums: 输入的整数列表
        :param k: 滑动窗口大小，用于计算平均值
        :return: 最大滑动窗口均值
        """
        
        # 初始化滑动窗口的前k个元素之和
        window_sum = sum(nums[:k])
        # 初始最大均值及起始位置索引
        max_avg, j = window_sum / k, 0
        
        # 滑动窗口遍历输入列表
        for i in range(k, len(nums)):
            # 更新滑动窗口的元素和
            window_sum += nums[i]
            window_sum -= nums[j]
            # 当前均值
            curr_avg = window_sum / k
            # 更新最大均值
            max_avg = max(curr_avg, max_avg)
            j += 1
        
        return max_avg

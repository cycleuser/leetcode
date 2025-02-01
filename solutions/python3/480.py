
class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :param nums: List[int] - 输入数组
        :param k: int - 窗口大小
        :return: List[float] - 滑动窗口的中位数序列
        
        该方法用于计算给定数组 nums 中长度为 k 的滑动窗口的中位数。
        
        方法步骤：
        1. 初始化第一个窗口，将其排序。
        2. 遍历整个数组，每次移除最左边的元素并插入当前遍历到的新元素。
        3. 计算并记录每个窗口的中位数。
        """
        window = sorted(nums[:k])  # 初始滑动窗口
        medians = []
        
        for a, b in zip(nums[:-k+1], nums[k-1:]):
            # 滑动窗口的中位数计算，取中间两个元素的平均值
            medians.append((window[k//2] + window[~(k//2)]) / 2.)
            
            # 移除滑动窗口最左边的元素
            window.remove(a)
            # 插入新元素，并保持有序性
            bisect.insort(window, b)
        
        return medians

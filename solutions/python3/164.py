
class Solution:
    def maximumGap(self, nums):
        """
        计算给定整数列表中最大差值。
        
        Args:
            nums (List[int]): 整数列表
        
        Returns:
            int: 最大差值
        
        1. 如果数字数量小于2，则直接返回0，因为至少需要两个元素才能计算差值。
        2. 初始化变量：n表示数组长度，mn和mx分别记录最小值与最大值。
        3. 计算桶大小bSize，以确保每个桶中的数据分布尽可能均匀。这里的+1是为了处理极端情况，例如所有数都相同的情况。
        4. 根据bSize计算需要的桶的数量bNum。
        5. 初始化桶列表buckets，每个桶由一个包含两个元素的列表表示，分别记录当前桶中的最小值和最大值。
        6. 遍历输入数组nums，将每个数字分配到相应的桶中，并更新该桶的最大最小值。
        7. 计算相邻桶之间的最大差值。如果某个桶为空，则将其与前一个桶合并。
        8. 返回找到的最大差值。
        """
        if len(nums) < 2:
            return 0
        
        n, mn, mx = len(nums), min(nums), max(nums)
        bSize = max(1, (mx - mn) // n + 1)
        bNum = (mx - mn) // bSize + 1
        buckets = [[float("inf"), -float("inf")] for _ in range(bNum)]
        
        for num in nums:
            ind = (num - mn) // bSize
            if num < buckets[ind][0]:
                buckets[ind][0] = num
            if num > buckets[ind][1]:
                buckets[ind][1] = num
        
        gap = 0
        for i in range(1, bNum):
            if buckets[i] == [float("inf"), -float("inf")]:
                buckets[i] = buckets[i - 1]
            gap = max(gap, buckets[i][0] - buckets[i - 1][1])
        
        return gap

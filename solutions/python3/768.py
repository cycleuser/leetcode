
class Solution:
    # 定义一个类来解决最大分块排序问题

    def maxChunksToSorted(self, arr):
        # 初始化最大值、最小值和结果计数器
        mx, mn = 0, 10 ** 9  # mx: 最大值, mn: 最小值
        res = 0  # 结果计数器

        # 遍历数组，确定每个分块的最大值
        for i in range(len(arr)):
            if arr[i] > mx:
                mx = arr[i]
            check[i][0] = mx  # 记录以i结尾的子数组的最大值
        
        # 反向遍历数组，确定每个分块的最小值
        mn = 10 ** 9  # 重置最小值
        for i in range(len(arr) - 1, -1, -1):
            check[i][1] = mn  # 记录以i开始的子数组的最小值
            if arr[i] < mn:
                mn = arr[i]

        # 统计满足条件的最大分块数量
        for c in check:
            if c[0] <= c[1]:
                res += 1  # 如果当前分块的最大值小于等于最小值，增加结果计数器

        return res  # 返回最大分块的数量


class Solution:
    # 定义一个类来解决最大距离问题

    def maxDistance(self, arrays):
        # 首先按照每个数组的第一个元素进行排序
        arrays.sort(key=lambda x: x[0])
        
        # 计算以第一个数组为基准的最大距离：最后一个数组的最后一个元素减去第一个数组的第一个元素
        d1 = max(arr[-1] for arr in arrays[1:]) - arrays[0][0]
        
        # 再次对数组进行排序，这次按照每个数组的最后一个元素进行排序
        arrays.sort(key=lambda x: x[-1])
        
        # 计算以最后一个数组为基准的最大距离：最后一个数组的最后一个元素减去第一个数组的第一个元素
        d2 = arrays[-1][-1] - min(arr[0] for arr in arrays[:-1])
        
        # 返回两个最大距离中的较大值
        return max(d1, d2)


class Solution:
    # 寻找每个区间的右区间，返回结果数组
    
    def findRightInterval(self, intervals):
        # 辅助函数：二分查找
        def binarySearch(l, r):
            x = intervals[l - 1].end
            found = None
            while l <= r:
                mid = (l + r) // 2
                if intervals[mid].start >= x:
                    r = mid - 1
                    found = mid
                else:
                    l = mid + 1
            return ind[intervals[found]] if found is not None else -1
        
        # 复制原数组并构建索引字典
        root = intervals[:]
        ind = {intr: i for i, intr in enumerate(root)}
        
        # 按区间起始位置排序
        intervals.sort(key=lambda x: x.start)
        
        # 遍历每个区间，使用二分查找确定其右区间，并在结果数组中存储索引
        for i in range(len(intervals)):
            root[ind[intervals[i]]] = binarySearch(i + 1, len(intervals) - 1)
        
        return root

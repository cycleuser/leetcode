
class Solution:

    def __init__(self, w):
        """
        初始化方法，构建权重对应的区间。
        
        参数：
        w (List[int]): 权重列表
        
        返回值：无
        """
        self.ranges, sm = [], 0
        for weight in w:
            # 将当前总和添加到区间起始位置
            self.ranges.append([sm, sm + weight])
            # 更新累积权重
            sm += weight
        # 定义查找范围的最小值和最大值
        self.mn, self.mx = 1, sm

    def pickIndex(self):
        """
        随机选择一个索引，其概率与对应的权重成正比。
        
        参数：无
        
        返回值：
        int: 按照权重随机选择的索引
        """
        num, l, r = random.randint(self.mn, self.mx), 0, len(self.ranges) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.ranges[mid][1] < num:
                # 如果中点右边界小于目标数，调整左边界
                l = mid + 1
            elif num <= self.ranges[mid][0]:
                # 如果目标数小于等于中点左边界，调整右边界
                r = mid - 1
            else:
                return mid

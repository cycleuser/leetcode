
class Solution:
    # 定义解决方案类

    def smallestRange(self, nums):
        # nums: List[List[int]] -> 二维数组，每个子数组为一个升序序列
        L = R = None
        # 初始化最小值L和最大值R为None
        
        while True:
            mn = mx = nums[0][-1]
            ind = [0]
            # 初始化最小值mn和最大值mx为第一个子数组的最后一个元素，索引列表ind初始化为包含起点0
            
            for i, ls in enumerate(nums[1:]):
                if ls[-1] > mx:
                    mx, ind = ls[-1], [i + 1]
                elif ls[-1] == mx:
                    ind.append(i + 1)
                elif ls[-1] < mn:
                    mn = ls[-1]
                # 遍历其他子数组，更新最大值mx和最小值mn，并记录对应的索引
            
            if L is None or mx - mn <= R - L:
                L, R = mn, mx
                # 如果L为None或当前区间比已有区间更小，则更新L和R
                
            for j in ind:
                nums[j].pop()
                if not nums[j]:
                    return [L, R]
                # 从满足条件的子数组中移除最后一个元素，若该子数组为空则返回[L,R]

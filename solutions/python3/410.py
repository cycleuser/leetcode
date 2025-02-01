
class Solution:
    # 定义一个辅助函数来验证分割方式是否满足条件
    def valid(self, mid: int) -> bool:
        cnt, sm = 0, 0
        for num in nums:
            sm += num
            if sm > mid:
                cnt += 1
                if cnt >= m: 
                    return False
                sm = num
        return True

    # 主函数，使用二分查找来找到满足条件的最小分割值
    def splitArray(self, nums, m):
        l, h = max(nums), sum(nums)  # 初始化搜索范围为数组中的最大值和所有元素之和
        while l < h:
            mid = (l + h) // 2  # 计算中间值
            if self.valid(mid): 
                h = mid  # 如果验证通过，缩小上限
            else: 
                l = mid + 1  # 否则增加下限
        return l  # 返回最终的分割值

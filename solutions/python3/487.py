
class Solution:
    # 定义一个解决方案类

    def findMaxConsecutiveOnes(self, nums):
        # 初始化左指针、零的位置和最大连续1的长度
        l, zero, mx = 0, -1, 0
        
        # 遍历数组加上一个虚拟的0，避免在边界处理
        for r, num in enumerate(nums + [0]):
            if not num:  # 如果当前数为0
                # 更新左指针、零的位置以及最大连续1的长度
                l, zero, mx = zero + 1, r, max(mx, r - l)
        
        return mx  # 返回最大连续1的长度

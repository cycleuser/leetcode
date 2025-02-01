
class Solution:
    # 定义一个类来解决两个数之和小于K的问题
    
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        # 对数组A进行排序，便于后续双指针操作
        A.sort()
        
        # 初始化结果变量res为-1（表示未找到符合条件的两数之和），左右指针l、r分别指向数组首尾
        res, l, r = -1, 0, len(A) - 1
        
        # 当左指针小于右指针时，继续循环
        while l < r:
            # 如果A[l] + A[r] >= K，则移动右指针r以尝试寻找更小的和
            if A[l] + A[r] >= K:
                r -= 1
            else:
                # 否则更新结果res，左指针l向右移动一位
                res = max(res, A[l] + A[r])
                l += 1
        
        # 返回最终的结果res
        return res

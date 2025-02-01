
class Solution:
    # 中文注释：实现计算非负整数x的平方根向下取整
    # English comment: Implement the calculation of the floor square root of a non-negative integer x
    
    def mySqrt(self, x: int) -> int:
        # 初始化左右指针，分别指向 0 和 x
        l, r = 0, x
        
        while l <= r:
            # 计算中间值 mid
            mid = (l + r) // 2
            
            # 如果 mid 的平方小于等于 x，则说明 mid 是当前范围内的候选解之一
            if mid * mid <= x:
                # 尝试向右扩大搜索区间，寻找可能更大的候选解
                l = mid + 1
            else:
                # 否则，缩小搜索区间到左半部分
                r = mid - 1
        
        # 最终返回右指针减一作为结果
        return l - 1


class Solution:
    # 定义一个类来解决最大面积问题

    def maxArea(self, height):
        # 初始化左右指针和最大面积
        left, right, mx = 0, len(height) - 1, 0
        
        while left < right:  # 当左指针小于右指针时循环
            # 计算当前宽度与高度的最小值乘以宽度作为面积，取其中的最大值
            mx = max(mx, (right - left) * min(height[left], height[right]))
            
            # 根据左右两侧的高度调整指针位置
            if height[left] < height[right]: 
                left += 1
            else: 
                right -= 1
        
        return mx  # 返回最大面积

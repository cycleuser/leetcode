
class Solution:
    # 定义一个解决方案类

    def trap(self, height):
        # 初始化结果变量res，左右边界字典left，以及左右最高点l和r
        res, left, l, r = 0, {}, 0, 0
        
        # 遍历height数组计算左侧最高墙的高度
        for i, h in enumerate(height):
            left[i] = l
            if h > l:
                l = h
        
        # 反向遍历height数组，计算储水量
        for i in range(len(height) - 1, -1, -1):
            roof = min(left[i], r)
            if roof > height[i]:
                res += roof - height[i]
            if height[i] > r:
                r = height[i]
        
        # 返回总的储水量
        return res

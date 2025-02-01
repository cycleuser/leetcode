
class Solution:
    # 定义一个方法来计算将n个点移动到目标位置t和s所需的最小距离
    
    def minDistance(self, height, width, t, s, n):
        # 计算当前布局下所有点到目标位置t的曼哈顿距离总和
        sm = 2 * sum(abs(x - t[0]) + abs(y - t[1]) for x, y in n)
        
        # 遍历每个点，找到将某个点移动到s位置时，最小化整体变化量的情况
        return min(
            sm - abs(x - t[0]) - abs(y - t[1]) + abs(x - s[0]) + abs(y - s[1])
            for x, y in n
        )
